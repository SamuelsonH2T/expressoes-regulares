import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
cel = (input('digite: '))

mo = phoneNumRegex.findall(cel)
print(mo)


'''
o metodo findall() retorna todas as correspondencias em uma string
em forma de lista. ex: ['111-222-1212']
se houver grupos na expressao regular ele retona uma lista de tuplas
contendo strings, uma para cada grupo
ex: [('122', '543', '2322'), ('123', '657', '8888')]
'''


phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
cel = (input('digite: '))

mo1 = phoneNumRegex2.findall(cel)
print(mo1)


