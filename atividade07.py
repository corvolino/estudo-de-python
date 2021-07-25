'''
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

basequadrado = float(input("\nQual a base do quadrado: "))
alturaquadrado = float(input("Qual a altura do quadrado: "))

area = basequadrado * alturaquadrado
dobroarea = pow(area, 2)

print("\nÁrea do quadrado = {}".format(area))
print("Dobro da área do quadrado = {}".format(dobroarea))