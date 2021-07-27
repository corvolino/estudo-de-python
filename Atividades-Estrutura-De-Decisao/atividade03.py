'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = input("\nInforme o Sexo por favor, F - Feminino, M - Masculino: ")
letra = letra.upper()
# variavel.upper() faz com que a string recebida em minusculo seja transformada em maiusculo

if letra == 'F':
    print("\nSexo Feminino !")
elif letra == 'M':
    print("\nSexo Masculino !")
else:
    print("\nSexo Inválido !")