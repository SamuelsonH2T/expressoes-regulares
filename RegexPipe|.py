import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo2 =  heroRegex.search('Tina Fey and Batman')
print(mo1.group())
print(mo2.group())

"""
uso do parenteses faz com que seja usado uma das correspondencias em destaque.
"""
#f = input('digite algo: ')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search(input('digite algo: '))
print(mo.group(1))