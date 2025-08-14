# Pytest Cheat Sheet

## Overview
Pytest is a Python testing framework designed for writing simple as well as scalable test cases.  
It provides:
- Automatic test discovery.
- Simple assertion syntax.
- Powerful features such as fixtures, parameterization, and markers.

---

## Installation
```bash
pip install pytest
````

---

## Running Tests

* Run all tests in the current directory:

```bash
pytest
```

* Run tests in a specific file:

```bash
pytest test_file.py
```

* Run a specific test function:

```bash
pytest test_file.py::test_function
```

* Show detailed output:

```bash
pytest -v
```

* Stop after first failure:

```bash
pytest -x
```

* Run only failed tests from the last run:

```bash
pytest --lf
```

---

## Naming Conventions

* **Test files:** `test_*.py` or `*_test.py`
* **Test functions:** Must start with `test_`
* **Test classes:** Must start with `Test` and not define `__init__`

---

## Basic Test Example

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Run with:

```bash
pytest test_math.py
```

---

## Assertions

Pytest uses Python's built-in `assert` statement:

```python
assert 2 + 2 == 4
assert "py" in "pytest"
assert len([1, 2, 3]) == 3
```

---

## Testing Exceptions

Use `pytest.raises` to verify exceptions:

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
```

---

## Fixtures (Setup/Teardown)

Fixtures provide reusable setup for tests:

```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3]

def test_list_append(sample_list):
    sample_list.append(4)
    assert sample_list == [1, 2, 3, 4]
```

The fixture runs before each test that uses it.

---

## Parametrized Tests

Run the same test with multiple inputs:

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

---

## Markers

Markers allow grouping or skipping tests:

```python
import pytest

@pytest.mark.slow
def test_long_running():
    pass

@pytest.mark.skip(reason="Feature not implemented")
def test_skip_example():
    pass

@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2
```

Run specific marker:

```bash
pytest -m slow
```

---

## Common Command-Line Options

| Option               | Description                |
| -------------------- | -------------------------- |
| `-v`                 | Verbose mode               |
| `-q`                 | Quiet mode                 |
| `-x`                 | Stop after first failure   |
| `--maxfail=N`        | Stop after N failures      |
| `--lf`               | Run only last failed tests |
| `--ff`               | Run failed tests first     |
| `--disable-warnings` | Suppress warnings output   |

---

## Example Folder Structure

```
project/
├── app/
│   └── main.py
└── tests/
    ├── test_main.py
    └── conftest.py  # shared fixtures
```

---

## References

* [Official Documentation](https://docs.pytest.org/)
* [Fixtures Guide](https://docs.pytest.org/en/stable/how-to/fixtures.html)
* [Assertion Examples](https://docs.pytest.org/en/stable/how-to/assert.html)

