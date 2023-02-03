
AGE = 1
"""
while AGE < 20:
    AGE += 4
    print(AGE)
"""
"""

# Creación de una lista de números
numbers = [1, 2, 3, 4, 5]

# Inicialización del índice
index = 0

# Bucle while para recorrer la lista de números
while index < len(numbers):
    # Imprimir el número actual en la lista

    if index >= 3:
      continue
    # Incrementar el índice para moverse al siguiente número en la lista
    print(numbers[index])
    index += 1
"""
    # Creación de una lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicialización del índice
index = 0

# Bucle while para recorrer la lista de números
while index < len(numbers):
    # Si el número actual es igual a 5, terminar el bucle
    if numbers[index] == 5:
        break
        
    # Si el número actual es igual a 3, saltar a la siguiente iteración
    if numbers[index] == 3:
        index += 1
        continue
        
    # Imprimir el número actual en la lista
    print(numbers[index])
    
    # Incrementar el índice para moverse al siguiente número en la lista
    index += 1