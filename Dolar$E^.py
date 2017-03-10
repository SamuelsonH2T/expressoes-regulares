import re

beginsWithHello = re.compile(r'Hello')
f = beginsWithHello.search('Hello World')
print(f)

'''
a string r'Hello' corresponde a strings que comecem com 'Hello'
'''


endswithNumber = re.compile(r'\d$')
g = endswithNumber.search('Your number is 42')
print(g)

'''
a string r'\d$' corresponde a strings que terminem com numeros de 0 a 9

'''



wholeStringIsNum = re.compile(r'^\d+$')
h = wholeStringIsNum.search('1234567890')
print(h)

'''
a string r'\d+$' corresponde a strings que terminem com um ou mais numeros de 0 a 9
'''