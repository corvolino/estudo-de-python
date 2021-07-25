'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
'''

numero1 = int(input("\nInforme o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))

primeiro = (pow(numero1, 2)) * (numero2 / 2)
segundo = (pow(numero1, 3)) + (pow(numero3, 3))
terceiro = pow(numero3, 3)

print("\nProduto do dobro do primeiro com metade do segundo = {:.2f}".format(primeiro))
print("Soma do triplo do primeiro com o terceiro = {}".format(segundo))
print("Terceiro elevado ao cubo = {:.2f}".format(terceiro))