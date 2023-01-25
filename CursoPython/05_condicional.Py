# Condicionales  if else elif


"""
if True:
    print('Deberia ejecutarse')
    if False:
        print('no se ejecuta')  
pet = input("what's is your favorite pet")

if pet == 'perro':
    print(f"that's good,its very nice your {pet}")
elif pet == 'gato':
    print(f"that's good,its very nice your {pet}")
elif pet == 'pez':
    print(f"that's good,its very nice your {pet}")
else:
    print("No tienes ninguna mascota buena")  
    """

num = int(input('introduce numero -> '))

ans = (num % 2)
print(ans)

if ans == 0:
    print(f'El numero -> {num} es par')
else:
    print(f'El numero -> {num} es impar')
"""
 ############ Ejemplo ya con else ################# 
stock = int(input("ingresa la cantidad de stock -> "))

if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
    print('El stock es incorrecto')
     
"""