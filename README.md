# Sentinel

Sentinel is a local-first coding assistant that uses semantic context distillation (RAG) and symbolic logic verification (Z3) to ensure code correctness.

## Philosophy

The tech industry has a blind spot. Everyone is sending entire codebases to giant remote models, praying for correct code, and accepting the hallucinations. Sentinel embraces the "overlooked" approach:

1.  **Local-First & Private:** Your code stays on your machine. We use local LLMs (like Ollama running Qwen or Phi3) for high-speed, private inference.
2.  **Semantic Context Distillation (RAG):** Stop sending 2,000 lines of code when only 50 matter. Sentinel uses Sentence-Transformers and ChromaDB to chunk, embed, and retrieve only the precise context needed. We use a sliding window approach to fetch the most relevant functions and their surroundings.
3.  **Symbolic Logic Verification:** "Vibes-based" coding is not enough. Sentinel uses formal verification via the Z3 Solver to guarantee code correctness. The AI must define pre-conditions and post-conditions, and Z3 mathematically proves whether the generated code holds up against edge cases.

## System Architecture

| Component | Responsibility | Tech Stack |
|---|---|---|
| Context Distiller | Semantic search & chunking | ChromaDB, Sentence-Transformers |
| Local Agent | Code generation & reasoning | Ollama (Qwen2.5-Coder) |
| Logic Guard | Formal Verification | Z3 Solver, Pydantic |
| Orchestrator | Managing the "Thought" loop | Python |

## Getting Started

1.  Install dependencies: `pip install -r requirements.txt`
2.  Run Ollama locally.
3.  Execute the main orchestrator: `python src/main.py`

## OpenClaw Integration

Sentinel includes a built-in OpenClaw skill (`skills/sentinel/SKILL.md`). If you use OpenClaw within this project directory, the agent will automatically recognize Sentinel and can mathematically verify code correctness or fix bugs using the orchestrator when requested.

To explicitly install the skill globally for OpenClaw so that it is available from any directory, you can copy and paste the following command to your OpenClaw agent:

```
Please install the OpenClaw skill located at ./skills/sentinel/SKILL.md by copying it to my global ~/.openclaw/skills/ directory.
```
