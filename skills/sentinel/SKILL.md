---
name: sentinel
description: A local-first coding assistant using semantic context distillation and symbolic logic verification.
metadata:
  openclaw:
    requires:
      bins:
        - python
---

# Sentinel

Sentinel is a local-first coding assistant that uses semantic context distillation (RAG) and symbolic logic verification (Z3) to ensure code correctness.

When the user asks you to verify code with Sentinel or fix a bug with Sentinel, run the orchestrator:

```bash
python src/main.py
```
