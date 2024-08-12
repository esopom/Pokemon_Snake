import os
import readchar
import random

POS_X = 0
POS_Y = 1

num = 1

obstacle_definition = """\
##########################   
#                           #
# ############  #### #    ### 
#         ###        ###    # 
#   ##### ### ##     ###    # 
#       # ### #    #####    # 
#     # # ### #     ######### 
#  ##   # ### # #     # ##### 
#   #   # ### # ####    ##### 
### #   # ### # ####    ##### 
### #   # ##            ##### 
###     #  ## ##     # # ##### 
### ### #  ## #         ##### 
#######   ### # # # #         
#############################\
"""

my_position = [6, 3]
tail_lenght = 0
tail = []
map_objects = []
position_end = [20,15]

# creat obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = 15

end_game = False
#generate random objects on the map
while len(map_objects) < num:
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

# Main loop
while not end_game:
    # Draw Map
    print("+" + "-" * MAP_WIDTH * 3 + "+")


    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None


            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1


                if tail_in_cell:
                    end_game = True



            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    # Ask user where he wants to move
    direction = readchar.readchar()

    new_position = my_position.copy()
    # MOVE
    if direction == "w":
        new_position[POS_Y] -= 1
        new_position[POS_Y] %= MAP_HEIGHT

    elif direction == "s":
        new_position[POS_Y] += 1
        new_position[POS_Y] %= MAP_HEIGHT

    elif direction == "a":
        new_position[POS_X] -= 1
        new_position[POS_X] %= MAP_WIDTH

    elif direction == "d":
        new_position[POS_X] += 1
        new_position[POS_X] %= MAP_WIDTH

    elif direction == "q":
        end_game = True

    # Check if the new position is not an obstacle before updating the player position
    if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position = new_position

    # new object
    if not map_objects:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
        while new_position in map_objects or new_position == my_position or obstacle_definition[new_position[POS_Y]][
            new_position[POS_X]] == "#":
            new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
        map_objects.append(new_position)

    os.system("cls")

print("\n" "Has muerto :)" "\n")