import re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #código de area
(\s|-|\.)? #separador
\d{3} #primeiros 3 digitos
(\s|-|\.) #separador
\d{4} #ultimos 4 digitos
(\s*(ext|x|ext.)\s*\d{2,5})? #extensao
)''', re.VERBOSE)

resp = input('Digite:')
mo = phoneRegex.search(resp)

print(mo.group())