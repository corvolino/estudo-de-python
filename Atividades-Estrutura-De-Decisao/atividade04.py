'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input("Qual a letra digitada: ")
letra = letra.upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print("\nLetra digitada é uma vogal !")

else:
    print("\nLetra digitada é uma consoante !")