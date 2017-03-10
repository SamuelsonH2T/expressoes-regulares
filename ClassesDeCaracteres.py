import re

xmasRegex = re.compile(r'\d+\s\w+')

resp = xmasRegex.findall('12 drummers, 11 pippers, 10 lords , 12 samucas , 10 ladies')
print(resp)


'''
minhas proprias classes de caracteres podem ser criadas
usando colchetes
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
resp2 = vowelRegex.findall('Robocop eats baby food')
print(resp2)


minhaRegex = re.compile(r'[a-zA-Z0-9]')

pergunta = input('digite:' )

resp3 = minhaRegex.findall(pergunta)
print(resp3)


print()
'''
podemos selecionar as classe que queremos por meio do
acento ^, que corresponderá a todas od caracteres que não estejam
na classe de caracteres.
'''


vowelRegex = re.compile(r'[^aeiouAEIOU]')
resp2 = vowelRegex.findall('Robocop eats baby food')
print(resp2)
