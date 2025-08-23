Num = int(input('Digite um numero inteiro positivo de 0 a 999: '))


while not (0 <= int(Num) <= 999):
    Num = int(input("Número inválido. Tente novamente digitar um número inteiro positivo de 0 a 999: "))


centena = Num[0] if len(Num) == 3 else '0'
dezena = Num[1] if len(Num) >= 2 else '0'
unidade = Num[2] if len(Num) == 3 else (Num[1] if len(Num) ==2 else Num[0])


print(f"O número {Num} tem a separação em {centena} centena, {dezena} dezena e {unidade} unidade")
