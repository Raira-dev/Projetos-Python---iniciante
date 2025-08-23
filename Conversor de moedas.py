valor_reais = float(input("Digite o valor em real para a conversão: "))

dolar_argentino = valor_reais / 5.70
euro = valor_reais / 6.18
peso_argentino = valor_reais / 0.01
libra_esterlina = valor_reais / 7.40
iene = valor_reais / 0.04

print(f"O valor de {valor_reais:.2f} reais, em outras moedas, é de aproximadamente: Dolar americano é {dolar_argentino:.2f} \n Euro é {euro:.2f} \n Peso argentino é {peso_argentino:.2f} \n Libra esterlina é {libra_esterlina:.2f} \n Iene japonês é {iene:.2f}")