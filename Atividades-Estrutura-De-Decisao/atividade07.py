'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

numero1 = float(input("Informe primeiro número: "))
numero2 = float(input("Informe segundo número: "))
numero3 = float(input("Informe terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("\nPrimeiro número é o maior valor!")
    if numero2 > numero3:
        print("\nTerceiro número é o menor!")
    else:
        print("\nSegundo número é o menor!")
elif numero2 > numero1 and numero2 > numero3:
    print("\nSegundo número é o maior valor!")
    if numero1 > numero3:
        print("\nTerceiro número é o menor!")
    else:
        print("\nPrimeiro número é o menor!")
else:
    print("\nTerceiro número é o maior valor!")
    if numero1 > numero2:
        print("\nSegundo número é o menor!")
    else:
        print("\nPrimeiro número é o menor!")