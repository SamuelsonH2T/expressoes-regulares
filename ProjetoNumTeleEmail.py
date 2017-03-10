import re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #código de area
(\s|-|\.)? #separador
\d{3} #primeiros 3 digitos
(\s|-|\.) #separador
\d{4} #ultimos 4 digitos
(\s*(ext|x|ext.)\s*\d{2,5})? #extensao
)''', re.VERBOSE)

text = '''

Nome: julia
Telefone: (232) 223-2111
E-mail: julia@hotmail.com
Nome: samuelson
Telefone: (231) 213-2411
E-mail: samu.elson@gmail.com
Nome: samu
Telefone: (122) 223-6111
E-mail: smww@gmail.com
Nome: juliana
Telefone: (232) 223-4511
E-mail: juliana@hotmail.com
Nome: samue
Telefone: (232) 223-2121
E-mail: samu@gmail
Nome: samuelllloo
Telefone: (232) 223-2178
E-mail: samuellllllllll2@hotmail.com
Nome: julia emanuele
Telefone: (232) 223-2109
E-mail: julinha@gmail.com
Nome: elba
Telefone: (232) 223-2183
E-mail: elba@hotmail.com

Nome: samuelson
Telefone: 232 223-2765
E-mail: samuca@gmail.com
Nome: xica
Telefone: (232) 223-2390
E-mail: xica@gmail.com

Nome: fulana
Telefone: (232) 223-2109
E-mail: fulana@gmail.com

Nome: samuelson max siqueira serra
Telefone: 122111334422
E-mail: samuelson@gmail.com

Nome: samuelson max
Telefone: 123445
E-mail: samuuu@gmail.com

'''

matches = []

for groups in phoneRegex.findall(text):
    matches.append(groups[0])

print(matches)


matches2 = []
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z0]{2,4})

)''' , re.VERBOSE)

for groups1 in emailRegex.findall(text):
    matches2.append(groups1[0])

print(matches2)