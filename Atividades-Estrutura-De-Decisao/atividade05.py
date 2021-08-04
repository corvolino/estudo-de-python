'''
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez
'''

nota1 = float(input("Qual a primeira nota: "))
nota2 = float(input("Qual a segunda nota: "))

media: float = (nota1 + nota2) / 2

if media >= 7.0 and media <= 9.9:
    print("\nAprovado")
elif media == 10:
    print("\nAprovado com Distinção")
else:
    print("\nReprovado")