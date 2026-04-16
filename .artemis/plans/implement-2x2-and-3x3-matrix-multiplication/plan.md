# Plan Name: Implement 2x2 and 3x3 Matrix Multiplication

## Tasks

### 1. Create matrix_2x2.py (Epic: Implement 2x2 and 3x3 matrix multiplication files)

#### Description

Create a standalone Python file `matrix_2x2.py` at the project root.

It must contain:
- A function `multiply(a, b)` that accepts two 2x2 matrices (each represented as a list of 2 lists of 2 numbers) and returns their product as a 2x2 matrix.
- Implementation using plain nested loops only — no NumPy or other libraries.
- A `if __name__ == '__main__':` block that demonstrates the function with two example 2x2 matrices and prints the result.

Example signature:
```python
def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    ...
```

#### Prompt

<general>
These instructions are for a task that is part of a larger plan:
    <plan>
    - previous (completed): N/A
    - current (in progress task): Create matrix_2x2.py <-
    - upcoming (not yet): Create matrix_3x3.py
    </plan>
Within reason, stick to only the deliverables outlined in these instructions,
don't do extra work, and instead assume anything not mentioned is out of scope.
</general>

Create `matrix_2x2.py` at the project root — a standalone Python file implementing 2x2 matrix multiplication using plain nested loops.

##### Technical Specs:
- **Language:** Python 3.8+
- **Location:** Project root (alongside `main.py`, `pyproject.toml`)
- **No external dependencies** — pure Python only, no NumPy or any imports

##### Implementation Checklist:
- [ ] Create `matrix_2x2.py` at the project root
- [ ] Implement `multiply(a, b)` accepting two 2x2 matrices (each a `list[list[float]]`) and returning a 2x2 `list[list[float]]`
- [ ] Use plain nested loops only — three nested `for` loops (row, col, inner) is the expected pattern
- [ ] Add a `if __name__ == '__main__':` block that defines two example 2x2 matrices, calls `multiply`, and prints the result
- [ ] Apply `black` and `isort` formatting

##### Success Criteria:
- [ ] `python matrix_2x2.py` runs without error and prints a valid 2x2 result
- [ ] The result of `multiply(a, b)` is mathematically correct for standard matrix multiplication — verify manually or against a known example (e.g. identity matrix × any matrix = that matrix)
- [ ] No imports are present in the file
- [ ] Function signature matches: `def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:`

##### Files to modify:
- `matrix_2x2.py` *(new file)*

---


### 2. Implement 2x2 and 3x3 matrix multiplication files

#### Description

Create two standalone Python files, each implementing matrix multiplication using plain nested loops (no NumPy). Each file should be independently runnable with a demonstration in a `__main__` block.


### 3. Create matrix_3x3.py (Epic: Implement 2x2 and 3x3 matrix multiplication files)

#### Description

Create a standalone Python file `matrix_3x3.py` at the project root.

It must contain:
- A function `multiply(a, b)` that accepts two 3x3 matrices (each represented as a list of 3 lists of 3 numbers) and returns their product as a 3x3 matrix.
- Implementation using plain nested loops only — no NumPy or other libraries.
- A `if __name__ == '__main__':` block that demonstrates the function with two example 3x3 matrices and prints the result.

Example signature:
```python
def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    ...
```

#### Prompt

<general>
These instructions are for a task that is part of a larger plan:
    <plan>
    - previous (completed): Create matrix_2x2.py
    - current (in progress task): Create matrix_3x3.py <-
    - upcoming (not yet): N/A
    </plan>
Within reason, stick to only the deliverables outlined in these instructions,
don't do extra work, and instead assume anything not mentioned is out of scope.
</general>

Create `matrix_3x3.py` at the project root — a standalone Python file implementing 3x3 matrix multiplication using plain nested loops. This mirrors the structure of `matrix_2x2.py` but for 3×3 inputs.

##### Technical Specs:
- **Language:** Python 3.8+
- **Location:** Project root (alongside `main.py`, `pyproject.toml`)
- **No external dependencies** — pure Python only, no NumPy or any imports

##### Implementation Checklist:
- [ ] Create `matrix_3x3.py` at the project root
- [ ] Implement `multiply(a, b)` accepting two 3x3 matrices (each a `list[list[float]]`) and returning a 3x3 `list[list[float]]`
- [ ] Use plain nested loops only — three nested `for` loops (row, col, inner) is the expected pattern
- [ ] Add a `if __name__ == '__main__':` block that defines two example 3x3 matrices, calls `multiply`, and prints the result
- [ ] Apply `black` and `isort` formatting

##### Success Criteria:
- [ ] `python matrix_3x3.py` runs without error and prints a valid 3x3 result
- [ ] The result of `multiply(a, b)` is mathematically correct — verify against a known example (e.g. identity matrix × any matrix = that matrix)
- [ ] No imports are present in the file
- [ ] Function signature matches: `def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:`

##### Files to modify:
- `matrix_3x3.py` *(new file)*

