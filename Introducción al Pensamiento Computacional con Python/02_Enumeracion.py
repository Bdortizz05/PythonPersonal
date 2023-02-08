

objetivo = int(input('escoge un entero: '))
RESPUESTA = 0

while RESPUESTA**2 < objetivo:
    print(RESPUESTA)
    RESPUESTA += 1

if RESPUESTA**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {RESPUESTA}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')
