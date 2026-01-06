from pathlib import Path
import pytest
from stl_splitter.core.validation import validate_angle, validate_input_file

# Tests for validate_angle

def test_validate_angle_type_error():
    """Non-numeric angle raises TypeError."""
    with pytest.raises(TypeError):
        validate_angle("not a number")

def test_validate_angle_out_of_range():
    """Out of range angle raises ValueError."""
    for val in [-10, 0, 180, 200]:
        with pytest.raises(ValueError):
            validate_angle(val)

def test_validate_angle_valid():
    """Valid angle returns float."""
    assert validate_angle(0.1) == 0.1
    assert validate_angle(90) == 90.0
    assert validate_angle(179.9) == 179.9

# Tests for validate_input_file

def test_validate_input_file_type_error():
    """Non-Path type raises TypeError."""
    with pytest.raises(TypeError):
        validate_input_file("string/path.stl")

def test_validate_input_file_not_found():
    """Missing file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        validate_input_file(Path("missing.stl"))

def test_validate_input_file_wrong_extension(tmp_path):
    """Non-STL extension raises ValueError."""
    f = tmp_path / "test.txt"
    f.write_text("")
    with pytest.raises(ValueError):
        validate_input_file(f)

def test_validate_input_file_valid(tmp_path):
    """Valid STL file returns Path."""
    f = tmp_path / "model.stl"
    f.write_text("")
    result = validate_input_file(f)
    assert result == f

def test_validate_input_file_case_insensitive(tmp_path):
    """.STL extension is accepted."""
    f = tmp_path / "model.STL"
    f.write_text("")
    result = validate_input_file(f)
    assert result == f
