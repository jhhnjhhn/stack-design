# Existing application migration example

Current: React, Spring Boot, PostgreSQL. Need: AI summaries.

Recommendation: `KEEP` the current stack and call the model API from Spring Boot. Add a small Python worker only if a required ML library cannot be operated reliably in Java. Do not rewrite the backend merely because AI examples often use Python.
