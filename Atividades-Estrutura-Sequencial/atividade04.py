'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota1 = float(input("\nInforme a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("\nValor da média é igual a {}".format(media))