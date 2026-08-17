#!/usr/bin/env python3
"""Detect technologies in root projects and bounded-depth monorepos with evidence."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


SKIP = {".git", ".hg", ".svn", "node_modules", ".venv", "venv", "dist", "build", ".next", "coverage", "vendor"}
MANIFESTS = {
    "package.json", "requirements.txt", "pyproject.toml", "go.mod", "pom.xml", "build.gradle", "build.gradle.kts",
    "Cargo.toml", "Dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml",
    ".gitlab-ci.yml", "Jenkinsfile", "serverless.yml", "serverless.yaml",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}


def version_text(value: object) -> str | None:
    return str(value) if isinstance(value, (str, int, float)) else None


def add(found: dict[tuple[str, str], dict], layer: str, name: str, evidence: Path, root: Path, version: str | None = None, confidence: str = "high") -> None:
    key = (layer, name)
    record = found.setdefault(key, {"technology": name, "version": version, "confidence": confidence, "evidence": []})
    relative = evidence.relative_to(root).as_posix()
    if relative not in record["evidence"]:
        record["evidence"].append(relative)
    if not record.get("version") and version:
        record["version"] = version


def manifests(root: Path, max_depth: int) -> list[Path]:
    result = []
    for current, dirs, files in os.walk(root):
        current_path = Path(current)
        depth = len(current_path.relative_to(root).parts)
        dirs[:] = [] if depth >= max_depth else [name for name in dirs if name not in SKIP and (not name.startswith(".") or name == ".github")]
        for name in files:
            if name in MANIFESTS or (current_path.name == "workflows" and name.endswith((".yml", ".yaml"))) or name.endswith(".tf"):
                result.append(current_path / name)
    return sorted(result)


def detect(root: Path, max_depth: int = 4) -> dict[str, list[dict]]:
    found: dict[tuple[str, str], dict] = {}
    js_map = {
        "react": ("frontend", "React"), "vue": ("frontend", "Vue"), "svelte": ("frontend", "Svelte"),
        "@angular/core": ("frontend", "Angular"), "next": ("frontend", "Next.js"), "nuxt": ("frontend", "Nuxt"),
        "astro": ("frontend", "Astro"), "vite": ("tooling", "Vite"), "@nestjs/core": ("backend", "NestJS"),
        "fastify": ("backend", "Fastify"), "express": ("backend", "Express"), "bullmq": ("queue", "BullMQ"),
        "ioredis": ("cache", "Redis"), "redis": ("cache", "Redis"), "pg": ("database", "PostgreSQL"),
        "mysql2": ("database", "MySQL"), "mongoose": ("database", "MongoDB"), "@prisma/client": ("data_access", "Prisma"),
        "@opentelemetry/api": ("observability", "OpenTelemetry"), "graphql": ("api", "GraphQL"), "@trpc/server": ("api", "tRPC"),
    }
    py_map = {
        "fastapi": ("backend", "FastAPI"), "django": ("backend", "Django"), "flask": ("backend", "Flask"),
        "celery": ("queue", "Celery"), "dramatiq": ("queue", "Dramatiq"), "redis": ("cache", "Redis"),
        "psycopg": ("database", "PostgreSQL"), "sqlalchemy": ("data_access", "SQLAlchemy"),
        "opentelemetry": ("observability", "OpenTelemetry"),
    }
    for path in manifests(root, max_depth):
        name = path.name
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()
        if name == "package.json":
            package = load_json(path)
            deps = {**package.get("dependencies", {}), **package.get("devDependencies", {})}
            for dep, (layer, technology) in js_map.items():
                if dep in deps:
                    add(found, layer, technology, path, root, version_text(deps[dep]))
        elif name in {"requirements.txt", "pyproject.toml"}:
            for token, (layer, technology) in py_map.items():
                match = re.search(rf"(?im)^\s*{re.escape(token)}(?:\[[^]]+\])?\s*(?:[=~<>!]+\s*)?([^\s,;]+)?", text)
                if match:
                    add(found, layer, technology, path, root, match.group(1), "medium" if name == "pyproject.toml" else "high")
        elif name == "go.mod":
            module = re.search(r"(?m)^go\s+(\S+)", text)
            add(found, "backend", "Go", path, root, module.group(1) if module else None)
        elif name == "pom.xml":
            add(found, "backend", "Spring Boot" if "spring-boot" in lower else "Java / Maven", path, root)
        elif name in {"build.gradle", "build.gradle.kts"}:
            add(found, "backend", "Spring Boot" if "org.springframework.boot" in lower else "Java or Kotlin / Gradle", path, root)
        elif name == "Cargo.toml":
            add(found, "backend", "Rust", path, root)
        elif name == "Dockerfile":
            add(found, "infrastructure", "Docker", path, root)
        elif name in {"docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml"}:
            add(found, "infrastructure", "Docker Compose", path, root)
            for token, layer, technology in (("postgres", "database", "PostgreSQL"), ("mysql", "database", "MySQL"), ("redis", "cache", "Redis"), ("rabbitmq", "queue", "RabbitMQ"), ("kafka", "queue", "Kafka"), ("minio", "storage", "MinIO")):
                if token in lower:
                    add(found, layer, technology, path, root, confidence="medium")
        elif name == ".gitlab-ci.yml":
            add(found, "cicd", "GitLab CI/CD", path, root)
        elif name == "Jenkinsfile":
            add(found, "cicd", "Jenkins", path, root)
        elif name in {"serverless.yml", "serverless.yaml"}:
            add(found, "infrastructure", "Serverless", path, root)
        elif path.parent.name == "workflows" and ".github" in path.parts:
            add(found, "cicd", "GitHub Actions", path, root)
        elif name.endswith(".tf"):
            add(found, "infrastructure", "Terraform", path, root)
            for token, technology in (("aws_", "AWS"), ("azurerm_", "Azure"), ("google_", "Google Cloud"), ("alicloud_", "Alibaba Cloud")):
                if token in lower:
                    add(found, "cloud", technology, path, root, confidence="medium")
        if name.endswith((".yml", ".yaml")) and ("apiversion:" in lower and "kind:" in lower):
            add(found, "infrastructure", "Kubernetes", path, root, confidence="medium")
    result: dict[str, list[dict]] = {}
    for (layer, _), record in sorted(found.items()):
        result.setdefault(layer, []).append(record)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--max-depth", type=int, default=4)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    result = detect(root, max(0, args.max_depth))
    if args.json:
        print(json.dumps({"root": str(root), "detected": result}, indent=2))
    else:
        print("Detected Stack")
        for layer, records in result.items():
            for record in records:
                version = f" {record['version']}" if record.get("version") else ""
                print(f"{layer.replace('_', ' ').title()}: {record['technology']}{version} [{record['confidence']}] <- {', '.join(record['evidence'])}")
        if not result:
            print("No supported stack markers found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
