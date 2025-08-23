def soma_e_conta_condicional():
    """
    Pede um número ao usuário e realiza duas operações:
    1. Soma todos os números ímpares de 1 até o número inserido (usando while).
    2. Conta quantos números pares múltiplos de 3 existem entre 1 e o número inserido (usando for).
    """
    while True:
        try:
            n = int(input("Digite um número inteiro n: "))
            if n >= 1:
                break
            else:
                print("Por favor, digite um número inteiro maior ou igual a 1.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
 
    # Parte 1: Somar números ímpares usando while
    soma_impares = 0
    contador_while = 1
    while contador_while <= n:
        if contador_while % 2 != 0:
            soma_impares += contador_while
        contador_while += 1
    print(f"Soma dos ímpares entre 1 e {n}: {soma_impares}")
 
    # Parte 2: Contar números pares múltiplos de 3 usando for
    quantidade_pares_multiplos_de_3 = 0
    for numero in range(1, n + 1):
        if numero % 2 == 0 and numero % 3 == 0:
            quantidade_pares_multiplos_de_3 += 1
    print(f"Quantidade de pares múltiplos de 3 entre 1 e {n}: {quantidade_pares_multiplos_de_3}")
 
if __name__ == "__main__":
    soma_e_conta_condicional()