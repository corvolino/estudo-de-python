'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!"
, conforme o caso.
'''

turno = input("Qual turno você estuda (M-matutino ou V-Vespertino ou N- Noturno): ")
turno = turno.upper()

if turno == 'M':
    print("\nBom Dia!")
elif turno == 'V':
    print("\nBoa Tarde!")
elif turno == 'N':
    print("\nBoa Noite!")
else:
    print("\nValor Inválido!")