
EATLIST = ['apple', 'bannana', 'cafe', 'tune', 'sugar']
print(type(EATLIST))
print('esta es la lista de comida ->', EATLIST)
EATLIST.append('rice')
EATLIST.append('chicken')
EATLIST.remove('bannana')
EATLIST.append('milk')
print('lilst->', EATLIST)
EATLIST.sort()
item = EATLIST.pop()
print('esta es la nueva lista de comida ->', EATLIST)
print(item)
eat_drink = ['juicy', 'beer', 'wine', 'wisky']
print('list drink->', eat_drink)
market = eat_drink + EATLIST
print(market)
eat_drink.extend(EATLIST)
print('add', eat_drink)
print(type(market))
