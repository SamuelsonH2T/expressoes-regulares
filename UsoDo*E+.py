'''
O uso do asterisco corresponde a uma ou mais ocorrencias
em um determinado padrão
'''

import re
try:
    batRegex = re.compile(r'Bat(wo)*man')
    resp = input('Digite algo: ')
    mo1 = batRegex.search(resp)
    print(mo1.group())
except AttributeError:
    print('a palavra %s não pertence ao padrao estabelecido.' % resp)




'''
uso do sinal de adição +
o sinal de adição é diferente, pois deve ter pelo menos
uma correspondencia no padrao estabelecido

'''

try:
    resp2 = input('digite algo para o sinal de  + :')
    batRegex2 = re.compile(r'Bat(wo)+man')
    mo2 = batRegex2.search(resp2)
    print(mo2.group())

except AttributeError:
    print('a palavra %s não pertence ao padrão especificado.' %resp2)





