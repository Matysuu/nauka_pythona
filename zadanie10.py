samolot = {'name': 'boeing',
           'przebieg': 10000,
           'type': 'pasazerski'}

print(samolot['name'])
print(samolot['type'])

print(samolot['nieznany_klucz'])
print(samolot.get('nieznany_klucz'))

for key in samolot:
    print('{0}:{1}'.format(key, samolot[key]))

in python2 samolot.iteritems()
for key, value in samolot.items():
    print("{0}:{1}".format(key, value))
