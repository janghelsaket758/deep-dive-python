# Purpose and Usage of `__init__.py` in Python Packages

**Audience:** developers creating small-to-medium Python projects who want clear guidance on when and how to use `__init__.py`.  
**Format:** explanation, practical examples, recommended patterns, and a short checklist for printing.

---

## 1. Short summary / elevator pitch

`__init__.py` is the file placed inside a directory to make that directory behave like a Python package. It can be an empty marker file, or it can contain light initialization code, metadata (like `__version__`), and re-exports that shape the package's public API. Keep it small and avoid heavy side effects (no long-running tasks, no training loops, no large I/O) — importing a package should be cheap and predictable.

---

## 2. Historical note & modern behaviour

- **Historically (pre-Python 3.3):** A directory required an `__init__.py` for Python to treat it as an importable package.
- **Modern Python (PEP 420):** Implicit namespace packages are allowed — a directory *can* be treated as a package without `__init__.py`.  
  However, many projects still include `__init__.py` for clarity, backwards compatibility, and to hold package-level code or metadata.

---

## 3. Common uses (with examples)

### 3.1. Mark the directory as a package (empty `__init__.py`)
When you only need the directory to be importable and want to avoid any package-level code.

```py
# src/__init__.py
# empty file or minimal docstring
"""Project `src` package."""
````

**Effect**

```py
import src        # works
from src import train  # will import submodule when accessible
```

---

### 3.2. Package metadata (version)

Expose a version string that other code and tests can read.

```py
# src/__init__.py
"""churn-project package."""

__version__ = "0.1.0"
```

Usage:

```py
import src
print(src.__version__)  # "0.1.0"
```

---

### 3.3. Convenience re-exports (shaping the public API)

Re-export frequently used names so callers can import from the package root. **Be careful**: re-exporting may import submodules at package import time and can cause circular imports or slow startup.

```py
# src/__init__.py
from .train import main  # re-export entrypoint

__all__ = ["main"]
```

Then users can do:

```py
from src import main
main(...)
```

**Caution:** if `train.py` executes heavy work on import, this will run during `import src` — avoid that.

---

### 3.4. Control `from package import *` via `__all__`

Define what symbols `from src import *` exposes.

```py
# src/__init__.py
__all__ = ["preprocess", "train"]
```

This does **not** automatically import `preprocess` and `train`; it controls only what is exported if those names are present in the package namespace.

---

### 3.5. Lazy imports (delay heavy imports until needed)

If you want convenience re-exports **without** the import-time cost, use lazy imports:

```py
# src/__init__.py
def _lazy_import_train():
    from .train import main
    return main

def main(*args, **kwargs):
    return _lazy_import_train()(*args, **kwargs)

__all__ = ["main"]
```

This keeps `import src` cheap and only loads `train` when `src.main()` is called.

---

### 3.6. Small package initialization (cautious)

You may run very small, safe initialization (e.g., set up logging defaults or import-time checks). Avoid I/O and network calls.

```py
# src/__init__.py
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = []
```

---

## 4. Examples: from minimal to more advanced

### Minimal (recommended default)

```py
# src/__init__.py
"""churn-project package."""
__version__ = "0.1.0"
__all__ = []
```

### Simple re-export (convenience)

```py
# src/__init__.py
"""churn-project package."""
from .train import main  # ok if train.py does not run heavy code at import
__all__ = ["main"]
__version__ = "0.1.0"
```

### Lazy re-export (safer)

```py
# src/__init__.py
"""churn-project package."""

__version__ = "0.1.0"

def main(*args, **kwargs):
    # import only when used
    from .train import main as _main
    return _main(*args, **kwargs)

__all__ = ["main"]
```

---

## 5. What *not* to put in `__init__.py`

* Long training loops, heavy computations, or long file reads.
* Network calls, opening large database connections, starting servers.
* Anything that has side effects users won't expect on a simple `import`.

If you need initialization that is expensive, provide an explicit function (e.g., `initialize_env()`) and call it intentionally in your CLI or application entrypoint.

---

## 6. Packaging & distribution notes

* `setuptools.find_packages()` discovers packages by the presence of `__init__.py`. (You can still use namespace packages, but including `__init__.py` is simple and explicit.)
* If you publish to PyPI and want `__version__` available to consumers, keeping it in `__init__.py` is conventional. Another option is to source it from a single place (e.g., `src/_version.py`) to avoid import-time side effects.

---

## 7. Testing and tooling recommendations

* Tests can import `__version__` to assert package version.
* Keep `__init__.py` import-time behaviour simple so test discovery and linting tools (mypy, pytest) are fast and deterministic.
* If linters or type-checkers import your package during checks, `__init__.py` should not run expensive or fragile code.

---

## 8. Troubleshooting tips

* **Circular imports**: if `__init__.py` imports submodules that import the package back, you will get import errors. Use lazy imports or move shared functions to a small module that both can import.
* **Slow imports**: profile import time (e.g., `python -X importtime -c "import src"`) and move heavy code out of `__init__.py`.
* **Namespace packages**: if you intentionally use PEP 420 implicit namespaces (multiple directories mapped to same package), omit `__init__.py`. Otherwise include it for compatibility.

---

## 9. Quick printable checklist

* [ ] Does the package need to run code at import? If yes, can it be deferred?
* [ ] Is there a clear `__version__` you want accessible? Put it here.
* [ ] Do you want to expose a small public API (few names)? Re-export carefully or use lazy imports.
* [ ] Are there any possible circular imports? Test imports in a fresh REPL.
* [ ] Keep file small and free of heavy I/O or network side effects.

---

## 10. Final recommendation (one-sentence)

Include a small `__init__.py` with only lightweight metadata (docstring and `__version__`), avoid automatic heavy work, and use lazy re-exports if you need convenience names without import-time cost.

---

## Appendix: Copy-ready examples

**Empty**

```py
# src/__init__.py
"""churn-project package."""
```

**Version only**

```py
# src/__init__.py
"""churn-project package."""
__version__ = "0.1.0"
```

**Safe re-export (lazy)**

```py
# src/__init__.py
"""churn-project package."""
__version__ = "0.1.0"

def main(*args, **kwargs):
    from .train import main as _main
    return _main(*args, **kwargs)

__all__ = ["main"]
```
