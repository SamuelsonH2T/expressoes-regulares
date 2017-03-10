import re
robocop = re.compile(r'robocop', re.I)
resp = robocop.search('Robocop is part man, part machine')
print(resp.group())

'''
re.I ou re.IGNORECASE, ignora as letras,
se estão escritas em maiusculas ou minusculas
'''
