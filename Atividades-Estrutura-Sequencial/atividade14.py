'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

pesopeixe = float(input("\nQual o peso dos peixes pescados: "))
taxa = 4.00
if pesopeixe > 50:
    excesso = pesopeixe - 50
    multa = excesso * taxa
    print("\nQuantidade de peixe pescasos em quilos = {:.2f} ".format(pesopeixe))
    print("Excesso de peso pescado = {:.2f} quilos".format(excesso))
    print("Valor da multa equivale a R$ {:.2f} reais".format(multa))
else:
    print("\nNão serã necessário pagar multa por excesso de peso!")
    multa = 0.00
    print("Quantidade de peixe pescasos em quilos = {:.2f} ".format(pesopeixe))

