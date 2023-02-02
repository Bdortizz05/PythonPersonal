
tup_names = ('BRAYAN', 'BRAYAN',  'DANILO', 'FELIPE','LUNA', 'VALERY')
print(type(tup_names))
# Verifica  si el nombre esta en la tupla
print('BRAYAN' in tup_names) 
# index(elemento): Devuelve el índice de la primera aparición de un elemento dado en la tupla.
indexone = tup_names.index('DANILO')
print(indexone)

# indexación
NAME = tup_names[1]
SURNAME = tup_names[2]
LSURNAME = SURNAME.lower()
LNAME = NAME.lower()

print(LSURNAME, LNAME)


for nombres in tup_names:
    if nombres == 'FELIPE' or nombres == 'LUNA':
        print(nombres)

INT = tup_names.count('BRAYAN')
print('Se repite -> ', INT)
