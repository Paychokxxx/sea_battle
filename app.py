from classes import Battlefield
import random 
import time #for debug
 
board_width = 10
board_heigth = 10

battlefield = Battlefield(board_width, board_heigth)
game_field = battlefield.create_field()

list_of_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]#[4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def start():
    print("Created field")
    print(*adding_ships(list_of_ships),sep='\n')

def is_fields_ccordinates_valid(vertical_ccordinate, horizontal_ccordinate, ship_lenght, horizontal_orientation):
    #valid = False

    for i in range(ship_lenght+2):
        try: 
            #print("cycle " + str(i))
            #print("ship_lenght " + str (ship_lenght))
            #print("horizontal_orientation is " + str(horizontal_orientation))
            if horizontal_orientation == True: 
                if horizontal_ccordinate-1+ship_lenght > 10:
                    #print("horizontal_orientation == True and horizontal_ccordinate+ship_lenght > 10:")
                    return False
                else: #horizontal_ccordinate-1+ship_lenght <= 10:
                    if game_field[vertical_ccordinate-1][horizontal_ccordinate-1+i] =='X': # check top row
                        #print("game_field[vertical_ccordinate-1][horizontal_ccordinate-1+i] =='X': # check top row")
                        return False
                    if game_field[vertical_ccordinate][horizontal_ccordinate-1+i] =='X': # check place of ship and heiberhood fields
                        #print("game_field[vertical_ccordinate][horizontal_ccordinate-1+i] =='X': # check place of ship and heiberhood fields")
                        return False
                    if game_field[vertical_ccordinate+1][horizontal_ccordinate-1+i] =='X': # check bottom row
                        #print("game_field[vertical_ccordinate+1][horizontal_ccordinate-1+i] =='X': # check bottom row")
                        return False


            else: #horizontal_orientation == False
                if vertical_ccordinate-1+ship_lenght > 10:
                    #print("horizontal_orientation == False and vertical_ccordinate+ship_lenght > 10:")
                    return False
                else: #vertical_ccordinate-1+ship_lenght <= 10:
                    if game_field[vertical_ccordinate-1+i][horizontal_ccordinate-1] =='X': # check left column
                        #print("game_field[vertical_ccordinate-1+i][horizontal_ccordinate-1] =='X': # check left column")
                        return False
                    if game_field[vertical_ccordinate-1+i][horizontal_ccordinate] =='X': # check place of ship and heiberhood fields
                        #print("game_field[vertical_ccordinate-1+i][horizontal_ccordinate] =='X': # check place of ship and heiberhood fields")
                        return False
                    if game_field[vertical_ccordinate-1+i][horizontal_ccordinate+1] =='X': # check right column
                            #print("game_field[vertical_ccordinate-1+i][horizontal_ccordinate+1] =='X': # check right column")
                            return False
        except IndexError:
            pass
            #print("Some Error. Lets try again")
    return True


def random_coordinates():
        vertical_ccordinate = random.randint(1, board_heigth)
        horizontal_ccordinate = random.randint(1, board_width)
        #print(vertical_ccordinate)
        #print(horizontal_ccordinate)

        return vertical_ccordinate, horizontal_ccordinate

def random_orientation():
    if random.randint(1, 2) == 1:
        orientation_is_horisontal = True
    else:
        orientation_is_horisontal = False

    return orientation_is_horisontal


def adding_ships(list_of_ships):
    for ship in list_of_ships:
        var_for_cycle=False
        while (not var_for_cycle):
            #time.sleep(0.45) # for debbug
            horizontal_orientation = random_orientation()
            vertical_ccordinate,horizontal_ccordinate = random_coordinates()
            var_for_cycle = is_fields_ccordinates_valid(vertical_ccordinate, horizontal_ccordinate, ship, horizontal_orientation)
            #print(is_fields_ccordinates_valid(vertical_ccordinate, horizontal_ccordinate, ship, horizontal_orientation))
            if not var_for_cycle: 
                pass
                #print("Cannot place a ship " + str(ship) + " there.")
                #print(*game_field,sep='\n')

        for i in range(ship):
            #print("+++++++++++" + str( is_fields_ccordinates_valid(vertical_ccordinate, horizontal_ccordinate, ship, horizontal_orientation)))
            if horizontal_orientation:
                game_field[vertical_ccordinate][horizontal_ccordinate+i] = 'X'
            else:
                game_field[vertical_ccordinate+i][horizontal_ccordinate] = 'X'

        #print(*game_field,sep='\n')
        #print("Ship was added to game field")

    return game_field


#print(*game_field,sep='\n')


if __name__=="__main__":
	start()
