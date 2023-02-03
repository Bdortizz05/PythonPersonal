#

COUNT_CPU = 0
COUNT_USER = 0

while True:
    player1 = (input('Ingrese "piedra, papel o tijera" player: '))
    cpu = (input('Ingrese "piedra, papel o tijera" cpu: '))

    if cpu == "papel" and player1 == "tijera" or cpu == "piedra" and player1 == "papel" or cpu == "tijera" and player1 == "piedra":
        COUNT_USER += 1
        print("Win player ->", COUNT_USER)
    elif cpu == "tijera" and player1 == "papel" or cpu == "piedra" and player1 == "tijera" or cpu == "papel" and player1 == "piedra":
        COUNT_CPU += 1
        print("Win cpu ->", COUNT_CPU)
    else:
        print("empate")

    if COUNT_CPU == 3 or COUNT_USER == 3:
        if COUNT_CPU == 3:
            print('Gana CPU')
        else:
            print('Gana player')
        break
