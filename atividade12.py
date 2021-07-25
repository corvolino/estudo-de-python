'''
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''

altura = float(input("\nQual sua altura: "))

pesoideal = (72.7 * altura) - 58

print("\nSeu peso é {:.2f} kilos".format(pesoideal))