from app import is_fields_ccordinates_valid, game_field

game_field[1][1] = 'X'


game_field[10][10] = 'X'

def test1(): #already existing ship
    
    assert is_fields_ccordinates_valid(1, 1, 4, True) == False
    assert is_fields_ccordinates_valid(2, 2, 4, False) == False
    assert is_fields_ccordinates_valid(10, 1, 10, True) == False
    assert is_fields_ccordinates_valid(1, 10, 10, False) == False
    return "test passed"

print(test1())