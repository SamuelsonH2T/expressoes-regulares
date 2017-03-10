import re

try:
    f = input('ditete algo: ')
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search(f)
    print(mo1.group())

except AttributeError:
    print('a palavra %s nao corresponde a o padrao especificado .' %f)


"""
uso do ? especifica que a palavra pode esta ou
nao dentro (opcional) de um padrao especificado
"""

