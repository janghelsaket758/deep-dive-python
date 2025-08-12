# Python Tooling Cheat Sheet (2025)

## Table 1 — Python Environment & Dependency Tooling (2025 MLOps Use Cases)

| Task / Use Case | Best Tool | Reason |
|-----------------|-----------|--------|
| Fastest install for Python-only deps | uv only | Rust speed, caching, lock files, modern. |
| Managing Python + native libs (e.g., CUDA, OpenCV) | conda | Handles non-Python binaries easily, NVIDIA packages. |
| All-in-one modern workflow (Python versions + deps) | rye only | Single tool, pyproject-based, modern. |
| Multiple Python versions only | pyenv only | Stable, proven version manager. |
| Stable Python versions + fast installs | pyenv + uv | Battle-tested combo, covers both speed & stability. |
| Legacy/simple projects with minimal deps | pip (normal) | Built-in, works everywhere, no extra setup. |
| Reproducible builds with lock file | uv only or rye only | Built-in lock support, no need for pip-tools. |
| Training on HPC or GPU cluster | conda | Better for GPU/CUDA dependency management. |
| Production Docker images | uv only | Minimal base image, fast CI/CD builds. |
| Cross-language projects (Python + R, C++) | conda | Package manager not tied to Python only. |
| Large legacy codebase already using requirements.txt | pip or pip + venv | Minimal changes, keep it simple. |

---

## Table 2 — Dependency Declaration Formats

| Feature / Use Case | requirements.txt | pyproject.toml |
|--------------------|------------------|----------------|
| Basic dependency listing | Yes | Yes |
| Pin exact versions for reproducibility | Yes (`pandas==2.1.1`) | Yes (via lock file) |
| Specify version ranges | Yes | Yes |
| Lock file support | No (needs pip-tools) | Yes (native in uv/rye/poetry) |
| PEP 518/621 standard | No | Yes |
| Project metadata (name, version, author) | No | Yes |
| Tool configuration in same file | No | Yes (sections for build, lint, test tools) |
| Ease of editing by hand | Yes (simple text file) | More structured, slightly verbose |
| Best for | Small/simple scripts, legacy projects | Modern projects, packaging, reproducibility |
| Future-proof | Legacy, still supported | Modern standard |

---
