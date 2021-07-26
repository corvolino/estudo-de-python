'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

arquivo = float(input("\nInforme o tamanho do arquivo em MB: "))
linkinternet = float(input("Informe o link da Internet: "))

conversaoMBparaKB = arquivo * 1000
converterinternet = linkinternet / 8

tempoestimado = (conversaoMBparaKB / converterinternet) / 60

print("\nTempo estimado do Download = {:.2f} minutos".format(tempoestimado))

