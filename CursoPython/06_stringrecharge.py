#


text  = 'she know programming in Python'
print('Python' in text)

print('python' in text)


if 'prueba' in text:
  print('thats correct of word-> Python')
elif 'python' in text:
  print('thats correct of word-> python')
else:
  print('its no correct word')

"""
Comandos para strings

Variable.upper()-> ponerlos  en mayuscuula
Variable.lower() ->  ponerlos en minuscula
len ->  peso  de el string 
Variable.count('a') ->  validar las veces que esta la letra 
"""

print('fin')
print(text.upper())
print(text.lower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith('he'))
print(text.replace('she', 'he'))

text_2 =  'este es un titulo'

print(text_2.capitalize())

print(text_2.title())

print(text_2.islower())