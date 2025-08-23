def analisar_temperaturas():
    """
    Simula a leitura de temperaturas em uma matriz 3x4 (3 semanas com 4 dias cada),
    calcula e exibe a média de cada semana, a maior e menor temperatura registrada,
    e a temperatura média geral.
    """
    matriz_temperaturas = []
    for semana in range(3):
        temperaturas_semana = []
        print(f"\n--- Semana {semana + 1} ---")
        for dia in range(4):
            while True:
                try:
                    temperatura = float(input(f"Digite a temperatura do dia {dia + 1}: "))
                    temperaturas_semana.append(temperatura)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        matriz_temperaturas.append(temperaturas_semana)
 
    # Calcular a média de cada semana
    medias_semanais = []
    for semana in matriz_temperaturas:
        media_semana = sum(semana) / len(semana)
        medias_semanais.append(media_semana)
        print(f"Média da Semana {matriz_temperaturas.index(semana) + 1}: {media_semana:.2f}°C")
 
    # Encontrar a maior e menor temperatura
    todas_temperaturas = [temp for semana in matriz_temperaturas for temp in semana]
    maior_temperatura = max(todas_temperaturas)
    menor_temperatura = min(todas_temperaturas)
    print(f"\nMaior temperatura registrada: {maior_temperatura:.2f}°C")
    print(f"Menor temperatura registrada: {menor_temperatura:.2f}°C")
 
    # Calcular a temperatura média geral
    media_geral = sum(todas_temperaturas) / len(todas_temperaturas)
    print(f"Temperatura média geral: {media_geral:.2f}°C")
 
if __name__ == "__main__":
    analisar_temperaturas()