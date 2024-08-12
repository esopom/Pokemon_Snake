import os
import random
import readchar

#Conbat variables
enemy_health = 10
my_health = 10

enemy_atack = None
my_atack = None

grafic_health_player = my_health * "#"
grafic_health_enemy = enemy_health * "#"

# Positions
POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 11

# User texts
start_banner = """\
#-------------------------------------------------------------------------------#
#                          Bienvenido a POKEMON SNAKE                           #
#                                                                               #
#-------------------------------------------------------------------------------#\
"""
obstacle_definition = """\
############################# 
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
###     #  ## ##     # # #### 
### ### #  ## #         ##### 
#######   ### # # # #       # 
############################# \
"""

# Lists
my_position = [3, 4]
trainers = [[3, 1], [15, 3], [27, 13]]
map_trainers = len(trainers)

# Start
print(start_banner)
name = input("Introduzca el nombre de su pokémon: ")

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

end_game = False
died = False

# Main loop
print(map_trainers)

while not end_game and not died:
    
    os.system("cls")
    
    #Condition end game
    if map_trainers == 0:
        break
    
    #Pokemons
    enemy = None
    selector = random.randint(1,3)
    
    if selector == 1:
        enemy = "Picachu"
        enemy_health = 10
    if selector == 2:
        enemy = "Charizard"
        enemy_health = 15
    if selector == 3:
        enemy = "Bulbasaur"
        enemy_health = 7


    # DRAW MAP2
    print("+" + "-" * (MAP_WIDTH*2) + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            trainer_in_cell = None
            for trainer in trainers:
                if trainer[POS_X] == coordinate_x and trainer[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    trainer_in_cell = trainer

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                if trainer_in_cell:
                    trainers.remove(trainer_in_cell)
                    map_trainers = map_trainers - 1
                    os.system("cls")
                    #Start combat
                    print("""
                                     +------------------------------------------------------------+
                                     |                                                            |                                                       
                                     |                  Has comenzado una batalla                 |
                                     |                         contra: {}                         |
                                     |                 (PULSA ENTER PARA CONTINUAR)               |        
                                     |                                                            |
                                     +------------------------------------------------------------+""".format(enemy))
                    input()
                    os.system("cls")
                    
                    #Combat process
                    
                    while enemy_health > 0 and my_health > 0:
                        print("Vida de {} = [{}]({})".format(name, grafic_health_player, my_health))
                        print("Vida de {} = [{}]({})".format(enemy, grafic_health_enemy, enemy_health))
                        input("(Presiona una tecla para continuar con el combate)")
                        enemy_atack = random.randint(1,3)
                        
                        if enemy_atack == 1:
                            print("{} ha usado ataque rápido".format(enemy))
                            my_health -=2
                        if enemy_atack == 2:
                            print("{} ha usado ataque cargado".format(enemy))
                            my_health -=4
                        if enemy_atack == 3:
                            print("{} ha usado guardia".format(enemy))
                            enemy_health +=2
                            
                        print("Vida de {} = [{}]({})".format(name, grafic_health_player, my_health))
                        print("Vida de {} = [{}]({})".format(enemy, grafic_health_enemy, enemy_health))
                        input("(Presiona enter para continuar con el combate)")
                        
                        user_choice_atack = input("Seleccione un ataque o defensa:\n" + 
                                                  "Ataque rapido: (Pulse r)\n"+ 
                                                  "Ataque cargado: (Pulse c)\n"+ 
                                                  "Guardia: (Pulse g)\n")
                        
                        if user_choice_atack == "r":
                            print("{} ha usado ataque rápido".format(name))
                            
                            enemy_health -=2
                        if user_choice_atack == "c":
                            print("{} ha usado ataque cargado".format(name))
                            enemy_health -=200
                        if user_choice_atack == "g":
                            print("{} ha usado guardia".format(name))
                            my_health +=2
                        else:
                            print("HAS USADO: NADA !")
                    
                    if my_health < 0:
                        died = True
                    if enemy_health < 0:
                        os.system("cls")
                        print("Has ganado esta batalla!!")
                        print("Combates restantes:{}".format(map_trainers))
                            
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * (MAP_WIDTH*2) + "+")
    
    #GUI USER
    print("COMBATES RESTANTES:{}".format(map_trainers))
    print("Vida de {} = [{}]({})".format(name, grafic_health_player, my_health))

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X],(my_position[POS_Y]-1) % MAP_WIDTH]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [(my_position[POS_X]-1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        print("Saliste del juego!")
        end_game = True
        
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

if died:
    os.system("cls")
    print("Has perdido!")
else:
    print("""
          +----------------+
          |   HAS GANADO ! |
          +----------------+
          """)



