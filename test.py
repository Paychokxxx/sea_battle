from app import is_fields_ccordinates_valid

def test():
    assert is_fields_ccordinates_valid(1, 1, 4, True) == True
    assert is_fields_ccordinates_valid(1, 1, 4, False) == True
    assert is_fields_ccordinates_valid(10, 10, 4, True) == False
    assert is_fields_ccordinates_valid(10, 10, 4, False) == False
    assert is_fields_ccordinates_valid(20, 20, 4, True) == False
    assert is_fields_ccordinates_valid(20, 20, 4, False) == False
    assert is_fields_ccordinates_valid(10, 9, 1, True) == True
    assert is_fields_ccordinates_valid(9, 10, 1, False) == True
    assert is_fields_ccordinates_valid(10, 9, 4, True) == False
    assert is_fields_ccordinates_valid(9, 10, 4, False) == False

    return "test passed"

print(test())