import os

import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]


while True:
    # DRAW MAP
    print("+"+"-" * (MAP_WIDTH * 3)+"+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        if my_position[POS_X] > 20:
            my_position[POS_X] = 0
            my_position[POS_Y] = my_position[POS_Y]
        elif my_position[POS_X] < 0:
            my_position[POS_X] = 20
            my_position[POS_Y] = my_position[POS_Y]
        for coordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")

            else:
                print("   ", end="")
        print("|")

    print("+"+"-" * (MAP_WIDTH * 3)+"+")

    #direction = input("Donde te quieres mover? [WASD]: ")

    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -=1
    elif direction == "s":
        my_position[POS_Y] +=1
    elif direction == "a":
        my_position[POS_X] -=1
    elif direction == "d":
        my_position[POS_X] +=1
    else:
        break

    os.system("cls")

