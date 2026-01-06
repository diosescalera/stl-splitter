from pathlib import Path

def validate_angle(angle: float) -> float:
    """Validate a numeric angle value in degrees."""
    if not isinstance(angle, (int, float)):
        raise TypeError("Angle must be numeric")
    if not (0 < angle < 180):
        raise ValueError("Angle must be between 0 and 180 degrees")
    return float(angle)

def validate_input_file(path: Path) -> Path:
    """Validate an input file path."""
    if not isinstance(path, Path):
        raise TypeError("Path must be a pathlib.Path")
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if path.suffix.lower() != ".stl":
        raise ValueError("Input file must have a .stl extension")
    return path
