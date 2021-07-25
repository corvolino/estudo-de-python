'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

'''

valorhora = float(input("\nQuanto ganha por hora trabalhada = "))
horatrabalhadames = float(input("Quantas horas trabalhadas por mês = "))

salario = valorhora * horatrabalhadames

print("\nValor do salário no mês = {:.2f} reais".format(salario))
