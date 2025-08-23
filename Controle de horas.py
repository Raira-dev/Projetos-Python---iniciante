#Controle de horas - ex: trabalho, atividade, estudos, etc.

from datetime import datetime

# Lista para guardar registros
registros = []

def registrar_horas():
    descricao = input("Descrição da atividade: ")
    inicio = input("Hora de início (HH:MM): ")
    fim = input("Hora de fim (HH:MM): ")

    try:
        h_inicio = datetime.strptime(inicio, "%H:%M")
        h_fim = datetime.strptime(fim, "%H:%M")

        duracao = h_fim - h_inicio
        horas = duracao.total_seconds() / 3600

        registro = {
            "descricao": descricao,
            "inicio": inicio,
            "fim": fim,
            "total_horas": round(horas, 2)
        }
        registros.append(registro)
        print("✅ Registro adicionado com sucesso!\n")

    except Exception as e:
        print("Erro: formato de hora inválido. Use HH:MM (ex: 09:30)")

def listar_registros():
    if not registros:
        print("Nenhum registro ainda.\n")
        return
    print("\n--- Registros ---")
    for i, r in enumerate(registros, 1):
        print(f"{i}. {r['descricao']} | {r['inicio']} - {r['fim']} | {r['total_horas']}h")
    print("")

# Loop principal
while True:
    print("1 - Registrar horas")
    print("2 - Listar registros")
    print("3 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        registrar_horas()
    elif opcao == "2":
        listar_registros()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida.\n")
