from collections import namedtuple

country = namedtuple('country', ['name', 'capital', 'continent'])

france = country('France', 'Paris', 'Europe')
japan = country('Japan', 'Tokyo', 'Asia')
senegal = country('Senegal', 'Dakar', 'Africa')

countries = (france, japan, senegal)
print(countries)
# print(france)
# print(japan)
# print(senegal)