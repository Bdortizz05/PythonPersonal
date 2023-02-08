my_str = 'pLaTzi'
len(my_str)

print('my_str = ' + my_str)
print('len(my_str) = ' + str(len(my_str)))
print(my_str[0:5])
print(my_str[5])
print(my_str.capitalize())
print(my_str.casefold())
print(len(my_str.center(20)),my_str.center(20))

contador_externo = 0
contador_interno = 0

while contador_externo < 11:
    while contador_interno < 11:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 10:
            break

    contador_externo += 1
    contador_interno = 0

