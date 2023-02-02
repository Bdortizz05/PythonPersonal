

STATUS= {
	'NAME':	['BRAYAN','FELIPE'],
	'SURNAME': ['ORTIZ', 'MARTINEZ'],
	'WEIGHT': (78, 80, 40),
	'AGE': (18, 19, 20, 21, 22),
	'STATUSMAR': (True, False), }
print(STATUS['NAME'])

person1	= STATUS['NAME'][1], STATUS['SURNAME'][1]
print(person1)

PERSON2= STATUS.get('NAME')[1]
STATUS['NAME'].append('PEPITO')
STATUS['SURNAME'].extend(['Gonzales', 'tamayo', 'juarez'])
print(PERSON2)
print(STATUS['NAME'],STATUS['SURNAME'])

