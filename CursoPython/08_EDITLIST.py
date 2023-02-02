#### 

eat_list = ['apple', 'bannana', 'cafe', 'tune','sugar']
print(type(eat_list))
print('esta es la lista de comida ->', eat_list)
eat_list.append('rice')
eat_list.append('chicken')
eat_list.remove('bannana')
eat_list.append('milk')
print('lilst->', eat_list)
eat_list.sort()
item = eat_list.pop()
print('esta es la nueva lista de comida ->', eat_list)
print(item)
eat_drink = ['juicy', 'beer', 'wine', 'wisky']
print('list drink->', eat_drink)
market = eat_drink + eat_list
print(market)
eat_drink.extend(eat_list)
print('add', eat_drink)
print(type(market))



