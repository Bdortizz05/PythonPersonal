#
player1 = (input('Ingrese "pieda,papel o tijera" : '))
cpu = (input('Ingrese "pieda,papel o tijera" : '))
player1 = player1.lower
cpu = cpu.lower
print(f"player= {player1}  cpu={cpu}")

if cpu == "papel" and player1 == "tijera" or cpu == "piedra" and player1 == "papel" or cpu == "tijera" and player1 == "piedra":
    print("Win player")
elif cpu == "tijera" and player1 == "papel" or cpu == "piedra" and player1 == "tijera" or cpu == "papel" and player1 == "piedra":
    print("Win cpu")
else:
    print("empate")
