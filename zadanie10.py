samolot = {'name': 'boeing',
           'przebieg': 10000,
           'type': 'pasazerski'}

# print(samolot['name'])
# print(samolot['type'])

# print(samolot.get('nieznany_klucz'))

for key in samolot:
    # print(key)
    print('{0}:{1}'.format(key, samolot[key]))

print('=========================')

for key, value in samolot.items():
    print("{0}:{1}".format(key, value))

print('=========================')

if 'name' in samolot:
    print("YES")

print('==========================')

if 'kola' not in samolot:
    print('NO')
