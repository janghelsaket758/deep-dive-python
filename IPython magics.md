# IPython magics: `%reload_ext autoreload` and `%autoreload 2`

# `%reload_ext autoreload` and `%autoreload 2` — usage, explanation, use cases, and related magics

## Usage (copy into the top cell of a Jupyter notebook)
```python
%reload_ext autoreload
%autoreload 2
````

## What these commands do (line by line)

* `%reload_ext autoreload`

  * Loads or reloads the IPython extension named `autoreload` into the current IPython/Jupyter session.
  * This makes the `autoreload` functionality available for use in that session.

* `%autoreload 2`

  * Configures the `autoreload` extension to mode `2`.
  * Mode meanings:

    * `0`: disable autoreload (default).
    * `1`: reload modules that are explicitly imported using `%aimport`.
    * `2`: reload **all** modules (except certain builtins/C-extension modules) automatically before executing each cell.

## Why use them together

* `%reload_ext autoreload` ensures the extension is loaded into the kernel.
* `%autoreload 2` activates automatic reloading in the broadest mode (reload all modules).
* Together they let you edit Python source files on disk (for example, modules inside your project `src/`) and immediately run notebook cells that import those modules without restarting the kernel or manually re-importing/reloading modules.

## Typical use cases

* Active development of local modules while iterating in a notebook (e.g., `src/data.py`, `src/models.py`).
* Quick experimentation where you change functions/classes in source files and want the notebook to see updates immediately.
* Teaching or demos where you modify code then re-run cells to show changes.

## Example (typical placement)

```python
# Top cell of notebook
%reload_ext autoreload
%autoreload 2

import pandas as pd
from src.data import load_raw, split_and_save  # edit src/data.py and changes will be picked up
```

## Important caveats and gotchas

* `autoreload` tries to update module objects in-place; this can **fail** or behave unexpectedly for:

  * objects created before a reload (e.g., existing class instances keep their old method bindings).
  * C-extension modules or compiled libraries (they are not reloadable).
  * complex import patterns (reloading does not rewrite references held by other modules).
* For class definition changes, objects created before the edit may still behave according to the old class; you may need to recreate instances.
* For deterministic behavior in production code, prefer restarting the kernel or using explicit import/reload workflows.
* `%autoreload 2` reloads a lot; if you want more control, use `%autoreload 1` + `%aimport modulename` for selected modules.
* Not a substitute for proper unit tests or CI — it is a developer convenience.

## Alternatives and related commands (useful magics)

* `%autoreload 1`

  * Reload only modules explicitly registered with `%aimport`.
  * Example:

    ```python
    %reload_ext autoreload
    %autoreload 1
    %aimport src.data
    ```

* `%aimport modulename`

  * Registers (or removes) modules for autoreload in mode `1`.

* `importlib.reload(module)` (regular Python)

  * Explicitly reload a specific module from Python standard library.
  * Example:

    ```python
    import importlib
    import src.data
    importlib.reload(src.data)
    ```

* `%load_ext <extension>`

  * Load an IPython extension (alias of `%reload_ext` for first load).
  * Example: `%load_ext autoreload`

* `%matplotlib inline` / `%matplotlib widget`

  * Configure matplotlib display in notebooks (`inline` creates static images; `widget` enables interactive backends).

* `%timeit`

  * Quick micro-benchmarking of small snippets.
  * Example: `%timeit my_function(x)`

* `%run script.py`

  * Run an external Python script in the current kernel (useful to execute scripts and keep variables in the session).

* `%who` / `%whos`

  * Inspect variables currently defined in the session.

* `%debug`

  * Enter post-mortem debugger after an exception.

## Minimal printable summary (one-liner)

Put these two lines at the top of a Jupyter notebook to auto-reload edited Python modules while you iterate:

```text
%reload_ext autoreload
%autoreload 2