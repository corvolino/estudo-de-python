'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''

produto1 = float(input("Informe valor do Primeiro produto: "))
produto2 = float(input("Informe valor do Segundo produto: "))
produto3 = float(input("Informe valor do Terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("\nVocê deve comprar o Primeiro produto!")
elif produto2 < produto1 and produto2 < produto3:
    print("\nVocê deve comprar o Segundo produto!")
else:
    print("\nVocê deve comprar o Terceiro produto!")
