import re


atRegex = re.compile(r'.at')
f = atRegex.findall('the cat latiu black hat mat calatvat')
print(f)


'''
correspondendo a tudo usando .* exceto a quebra de linha
o padrao passado a re.compile() deve ser seguido em
nameRegex.search(),como em First Name: e Last Name:
'''

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Samuel Last Name: siqueira')
print(mo.group(1))


'''
passando re.DOTALL, podemos fazer o .* corresponder a
todos os caracteres, inclusive o de quebra de linha
'''

noNewlineRegex = re.compile('.*')
resp = noNewlineRegex.search('Serve the public trust.\nProtect the inocent.\nUphold the law.')
print(resp.group())

print()
'''
usando re.DOTALL
'''

noNewlineRegex2= re.compile('.*', re.DOTALL)
resp2 = noNewlineRegex2.search('Serve the public trust.\nProtect the inocent.\nUphold the law.')
print(resp2.group())
