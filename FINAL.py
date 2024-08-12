import random
import readchar
import os

map_draws = """\
#######################################
#                                     #
####################################  #
           #                       #   
#################################  #  #
#####                          ##  #  #
############################   ##  #  #
#####                          ##  #  #
########################   ######  #  #
###                            #      #
############################   #   ####
#                                     #
######   ##############################
# #                                   #
###  ##################################
###                               #   #
###############################   #   #
###                               #   #
###############################   #   #
#################                     #
#######################################\
"""
map_draws = [list(row) for row in map_draws.split("\n")]

POS_X = 0
POS_Y = 1
MAP_WIDTH = len(map_draws[0])
MAP_HEIGTH = len(map_draws)
my_position = [2, 1]
fight_spots = [[34, 1], [4, 3], [6, 5], [6, 7], [4, 9], [36, 13], [36, 15], [4, 17]]
final_boss = [[18, 19]]
map_trainers = len(fight_spots)
final_boss_acces = False

vida_final_boss = 100
fuerza_jugador = 2
vida_jugador_jefe = 15
juador = input("Cual nombre seleccionas para tu personaje: ")
enemy = None
end_game = None
final_boss_monster = "Mario goku"

# principal loop:
print(map_trainers)

while True:
    # begining of map
    print("+" + "-" * MAP_WIDTH * 1 + "+")
    for coordinate_y in range(MAP_HEIGTH):
        print("|", end="")

        random_enemy_choose = (random.randint(1, 8))
        if random_enemy_choose == 1:
            enemy = "charizard"
        elif random_enemy_choose == 2:
            enemy = "gorila"
        elif random_enemy_choose == 3:
            enemy = "rocky"
        elif random_enemy_choose == 4:
            enemy = "squirtle"
        elif random_enemy_choose == 5:
            enemy = "pikachu"
        elif random_enemy_choose == 6:
            enemy = "flower"
        elif random_enemy_choose == 7:
            enemy = "mew"
        elif random_enemy_choose == 9:
            enemy = "rat"
        vida_enemy = 10

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            fights_in_cell = None
            fights_in_cell_boss = None

            for fights in fight_spots:
                if fights[POS_X] == coordinate_x and fights[POS_Y] == coordinate_y:
                    char_to_draw = "O"
                    fights_in_cell = fights

            for final_monster in final_boss:
                if final_monster[POS_X] == coordinate_x and final_monster[POS_Y] == coordinate_y:
                    char_to_draw = "8"
                    fights_in_cell_boss = final_monster

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if fights_in_cell:
                    fight_spots.remove(fights_in_cell)
                    os.system("cls")
                    map_trainers -= 1

                    input("""
                                     +------------------------------------------------------------+
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     |                  Has entrado a una batalla                 |
                                     |                         contra {}                          |
                                     |                    Enter for continue.                     |
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     |                                                            |
                                     +------------------------------------------------------------+""".format(enemy))
                    os.system("cls")
                    vida_enemy = 10
                    vida_jugador = 10
                    vida_muestra_jugador = vida_jugador * "#"
                    vida_muestra_enemy = vida_enemy * "#"

                    ########################CPU  ATTACKS----
                    while vida_jugador >= 0 or vida_enemy >= 0:

                        ataque_enemy = random.randint(1, 3)

                        if ataque_enemy == 1:
                            print("{} te lanza un Golpe fuerte\n".format(enemy))
                            vida_jugador -= 1
                            if vida_jugador <= 0:
                                vida_jugador = 0
                            vida_muestra_jugador = vida_jugador * "#"
                            vida_muestra_enemy = vida_enemy * "#"
                            print("la vida de {} a bajado.\n".format(juador))
                            print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                            print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))

                        elif ataque_enemy == 2:
                            print("{} deside curarse \n".format(enemy))
                            vida_enemy += 1
                            if vida_jugador <= 0:
                                vida_jugador = 0
                            vida_muestra_jugador = vida_jugador * "#"
                            vida_muestra_enemy = vida_enemy * "#"
                            print("la vida de {} a subido.\n".format(enemy))
                            print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                            print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))

                        else:
                            print("{} te lanza una un gran golpe de energia\n".format(enemy))
                            vida_jugador -= 1
                            if vida_jugador <= 0:
                                vida_jugador = 0
                            vida_muestra_jugador = vida_jugador * "#"
                            vida_muestra_enemy = vida_enemy * "#"
                            print("la vida de {} a bajado.\n".format(juador))
                            print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                            print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))

                        if vida_jugador <= 0:
                            vida_jugador = 0
                            vida_muestra_jugador = vida_jugador * "#"
                            vida_muestra_enemy = vida_enemy * "#"
                            print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                            print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))
                            input("Has perdido la lucha vuelve a intentarlo\n"
                                  "Press enter to exit.")
                            exit()

                            # turno de jugador
                        input("Es tu turno de atacar (Press enter to atack) \n")
                        os.system("cls")

                        ataque_jugador = None
                        ########################PLAYER ATTACKS----
                        while ataque_jugador != "a" and ataque_jugador != "b" and ataque_jugador != "c" and ataque_jugador != "d":
                            ataque_jugador = (input(" Cual los siguientes ataques deseas realizar :\n"
                                                    "a: golpe triple\n"
                                                    "b: golpe giratorio \n"
                                                    "c: patada aerea \n"
                                                    "d: no hacer nada.\n"
                                                    "Respuesta : \n"))
                            if ataque_jugador == "a":
                                print("{} lanza su golpe triple y acierta\n".format(juador))
                                vida_enemy -= 2
                                if vida_enemy <= 0:
                                    vida_enemy = 0

                                vida_muestra_jugador = vida_jugador * "#"
                                vida_muestra_enemy = vida_enemy * "#"
                                print("la vida de {} a bajado.\n".format(enemy))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))

                            elif ataque_jugador == "b":
                                print("golpe giratorio ha sido efectivo \n")
                                vida_enemy -= 2
                                if vida_enemy <= 0:
                                    vida_enemy = 0

                                vida_muestra_jugador = vida_jugador * "#"
                                vida_muestra_enemy = vida_enemy * "#"
                                print("la vida de {} a bajado.\n".format(enemy))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))


                            elif ataque_jugador == "c":
                                print(
                                    "OH NO, {} solo sabe dar puños intenta dar una patada y cae. !te inflijes daño\n".format(
                                        juador))
                                vida_jugador -= 1
                                if vida_enemy <= 0:
                                    vida_enemy = 0
                                vida_muestra_jugador = vida_jugador * "#"
                                vida_muestra_enemy = vida_enemy * "#"
                                print("la vida de {} a bajado.\n".format(juador))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))

                                input("Presionona enter para continuar \n")

                            elif ataque_jugador == "d":
                                print(" {} decide esperar y curarte".format(juador))
                                vida_jugador += 1

                                vida_muestra_jugador = vida_jugador * "#"
                                vida_muestra_enemy = vida_enemy * "#"

                                print("la vida de {} a subido.\n".format(juador))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))

                            os.system("cls")

                        if vida_enemy <= 0:
                            vida_enemy = 0
                            print("{} a ganado la batalla y te has vuelta mas fuerte".format(juador))
                            print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                            print("Vida de {} = [{}]({})".format(enemy, vida_muestra_enemy, vida_enemy))
                            input("press enter to coninue: ")
                            os.system("cls")
                            break

                        elif vida_jugador <= 0:
                            input("has perdido y te retiras del pueblo\n"
                                  "Press enter to exit.")
                            exit()

                    if map_trainers <= 0:
                        final_boss_acces = True
                        ataque_unico = input("""
                                                +------------------------------------------------------------+
                                                |            Has ganado todas las batallas:                  |
                                                |                                                            |
                                                |             cual de los siguientes poderes deseas?:        |
                                                |                                                            |
                                                |      a: ataque: amuenta tu daño en gran medida.            |
                                                |      b: tu salud aumenta en gran medida                    |
                                                |      c: aura del paladin: sube tu salud y tu fuerza        |
                                                |                                                            |
                                                |                                                            |
                                                |                                                            |
                                                |                                                            |
                                                +------------------------------------------------------------+""")
                        os.system("cls")

                        if ataque_unico == "a":
                            fuerza_jugador += 3
                        elif ataque_unico == "b":
                            vida_jugador_jefe += 15
                        elif ataque_unico == "c":
                            fuerza_jugador += 2
                            vida_jugador_jefe += 10

                    #####finnnn pelea.

                if fights_in_cell_boss:
                    final_boss.remove(fights_in_cell_boss)
                    if final_boss_acces == False:
                        input("no eres digno de esta batalla.")
                        exit()
                    elif final_boss_acces == True:
                        os.system("cls")
                        input("""
                                        +------------------------------------------------------------+
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                           {}                               |
                                        |               DESEAS DESAFIAR A MARIO GOKU                 |
                                        |                   enter para continuar                     |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        +------------------------------------------------------------+""".format(
                            juador))
                        os.system("cls")

                        vida_jugador = 25 + vida_jugador_jefe
                        vida_final_boss = 100
                        vida_muestra_jugador = vida_jugador * "#"
                        vida_muestra_final_boss = vida_final_boss * "#"
                        ataque_jugador = None

                        while vida_jugador >= 0 or vida_final_boss >= 0:

                            ataque_final_boss = random.randint(1, 3)

                            if ataque_final_boss == 1:
                                print("{} te lanza una navaja imbuida de energia\n".format(final_boss_monster))
                                vida_jugador -= 3
                                if vida_jugador <= 0:
                                    vida_jugador = 0
                                    vida_muestra_jugador = vida_jugador * "#"
                                    vida_muestra_final_boss = vida_final_boss * "#"

                                print("la vida de {} a bajado.\n".format(juador))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(enemy, vida_muestra_final_boss, vida_final_boss))
                            elif ataque_final_boss == 2:
                                print("{} te lanza una onda vital\n".format(final_boss_monster))
                                vida_jugador -= 4
                                if vida_jugador <= 0:
                                    vida_jugador = 0
                                    vida_muestra_jugador = vida_jugador * "#"
                                    vida_muestra_final_boss = vida_final_boss * "#"

                                print("la vida de {} a bajado.\n".format(juador))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(enemy, vida_muestra_final_boss, vida_final_boss))
                            elif ataque_final_boss == 3:
                                print("{} Vuela por los aires y se regenera\n".format(final_boss_monster))
                                vida_final_boss += 2
                                vida_muestra_jugador = vida_jugador * "#"
                                vida_muestra_final_boss = vida_final_boss * "#"
                                print("la vida de {} a bajado.\n".format(juador))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(enemy, vida_muestra_final_boss, vida_final_boss))

                            if vida_jugador <= 0:
                                vida_jugador = 0
                                input("Has perdido esta batalla.\n"
                                      "press enter to exit.")
                                exit()

                            input("tu turno de atacar\n"
                                  "press enter to continue")
                            os.system("cls")

                            # player turn

                            ataque_jugador = input(" Cual los siguientes ataques deseas realizar :\n"
                                                   "a: golpe triple\n"
                                                   "b: golpe giratorio \n"
                                                   "c: patada aerea \n"
                                                   "d: no hacer nada.\n"
                                                   "Respuesta : \n")

                            if ataque_jugador == "a":
                                print(" {} Lanza un golpe triple\n".format(juador))
                                print("{} pierde vida".format(final_boss_monster))
                                vida_final_boss -= 5 * fuerza_jugador
                                if vida_final_boss <= 0:
                                    vida_final_boss = 0
                                print("la vida de {} a bajado.\n".format(final_boss_monster))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(final_boss_monster, vida_muestra_final_boss,
                                                                     vida_final_boss))
                            elif ataque_jugador == "b":
                                print(" {} Lanza un golpe giratorio\n".format(juador))
                                print("{} pierde vida".format(final_boss_monster))
                                vida_final_boss -= 4 * fuerza_jugador
                                if vida_final_boss <= 0:
                                    vida_final_boss = 0

                                print("la vida de {} a bajado.\n".format(final_boss_monster))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(final_boss_monster, vida_muestra_final_boss,
                                                                     vida_final_boss))
                            elif ataque_jugador == "c":
                                print(" {} Lanza una patada aerea mejorada \n".format(juador))
                                print("{} pierde vida".format(final_boss_monster))
                                vida_final_boss -= 7 * fuerza_jugador
                                if vida_final_boss <= 0:
                                    vida_final_boss = 0

                                print("la vida de {} a bajado.\n".format(final_boss_monster))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(final_boss_monster, vida_muestra_final_boss,
                                                                     vida_final_boss))
                            elif ataque_jugador == "d":
                                print(" {} se retira a regenerarce\n".format(juador))
                                print("{} regenera vida".format(juador))
                                vida_jugador += 5

                                print("la vida de {} a subido.\n".format(juador))
                                print("Vida de {} = [{}]({})".format(juador, vida_muestra_jugador, vida_jugador))
                                print("Vida de {} = [{}]({})".format(final_boss_monster, vida_muestra_final_boss,
                                                                     vida_final_boss))

                            if vida_final_boss <= 0:
                                os.system("cls")
                                input("""
                                              +------------------------------------------------------------+
                                              |                                                            |
                                              |                                                            |
                                              |                                                            |
                                              |                                                            |
                                              |                                                            |
                                              |                  Has derrotado al terror                   |
                                              |                  del pueblo ya no hay mas                  |
                                              |                  enemigos con lo cual puedas               |
                                              |                  luchar ahora eres el rey                  |
                                              |                                                            |
                                              |                           fin.                             |
                                              |                                                            |
                                              |                                                            |
                                              +------------------------------------------------------------+""")
                                exit()

            if map_draws[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            print("{}".format(char_to_draw), end=(""))
        print("|")
    print("+" + ("-" * MAP_WIDTH) * 1 + "+")

    # movement:
    print("W,A,S,D TO MOVE")
    print(map_trainers)

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "e":  # <-- Exit
        print("Has salido del juego")
        end_game = True

    if new_position:
        if map_draws[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")

    if end_game == True:
        os.system("cls")
        input("""
                                        +------------------------------------------------------------+
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                      You are Dead                          |
                                        |                  Press enter to exit                       |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        |                                                            |
                                        +------------------------------------------------------------+""")