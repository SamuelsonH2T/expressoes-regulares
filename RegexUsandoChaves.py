import re

try:
    f = input('digite: ')
    haRegex = re.compile(r'(ha){1,}')
    mo = haRegex.search(f)
    print(mo.group())

except AttributeError:
    print('o padrao %s não é valido.' %f)

'''
uso de chaves serve para repetir um
grupo () determinado numero {} de vezes
No exemplo acima, o grupo(ha) vai ser repetido
de 1 a quantas vezes dor digitado o mesmo.
'''