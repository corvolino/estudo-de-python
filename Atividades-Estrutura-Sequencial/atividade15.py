'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

valorhora = float(input("\nQuanto você recebe por hora trabalhada: "))
horastrabalhadas = float(input("Quantas horas trabalhou nesse mês: "))

salariobruto = valorhora * horastrabalhadas
ir = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
salarioliquido = salariobruto - ir - inss - sindicato

print("\nSalário Bruto = {:.2f} Reais".format(salariobruto))
print("Valor pago ao IR (11%) {:.2f} Reais".format(ir))
print("Valor pago ao INSS (8%) = {:.2f} Reais".format(inss))
print("Valor pago ao Sindicato (5%) = {:.2f} Reais".format(sindicato))
print("\nValor do Salário Líquido = {:.2f} Reais".format(salarioliquido))