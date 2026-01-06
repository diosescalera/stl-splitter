# Validation

Input validation utilities used by the core logic.

## `validate_angle(angle: float) -> float`

Validates a numeric angle value in degrees.

- **Checks**
  - Value is numeric (int or float)
  - Value is strictly between 0 and 180 degrees (0 < angle < 180)

- **Raises**
  - `TypeError` — non-numeric value
  - `ValueError` — value out of range (must be 0 < angle < 180)

- **Returns**
  - Angle as `float`

---

## `validate_input_file(path: Path) -> Path`

Validates an input file path.

- **Checks**
  - `path` is a `pathlib.Path` instance
  - File exists on filesystem
  - File extension is `.stl` (case-insensitive)

- **Raises**
  - `TypeError` — invalid type
  - `FileNotFoundError` — file does not exist
  - `ValueError` — invalid extension

- **Returns**
  - Validated `Path`
