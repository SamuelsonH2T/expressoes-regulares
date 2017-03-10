import re
namesRegex = re.compile(r'Agent \w+')
resp = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob. ')

print(resp)

'''
\w corresponde a qq caractere, digito, pense nisso
como um caractere de palavras

'''
agentNamesRegex = re.compile(r'Agent (\w)\w*')
resp2 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew. ')
print(resp2)