import re

phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumberRegex.search('My number is (415) 555-4243')

print(mo.group())
'''

areaCode, mainNumber = (mo.groups())
print(areaCode)
print(mainNumber)
'''
'''
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
adicionando parenteses, e imprimindo os valores aparecera os grupos
ex: print(mo.group(1))
'415'
'''

