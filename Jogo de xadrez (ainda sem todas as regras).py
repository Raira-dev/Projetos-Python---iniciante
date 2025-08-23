# Representação bem simples de um tabuleiro de xadrez

# Cada peça é representada por 1 letra maiúscula (branco) ou minúscula (preto)
# P/p = Peão, R/r = Torre, N/n = Cavalo (Knight), B/b = Bispo, Q/q = Rainha, K/k = Rei

def criar_tabuleiro():
    return [
        ["r","n","b","q","k","b","n","r"],  # Pretas
        ["p","p","p","p","p","p","p","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["P","P","P","P","P","P","P","P"],
        ["R","N","B","Q","K","B","N","R"]   # Brancas
    ]

def mostrar_tabuleiro(board):
    print("  a b c d e f g h")
    for i, linha in enumerate(board):
        print(8-i, " ".join(linha), 8-i)
    print("  a b c d e f g h")

def mover(board, origem, destino):
    """Movimenta peça de origem para destino (ex: 'e2' -> 'e4')"""
    colunas = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}

    try:
        # Converter posições
        o_col, o_lin = colunas[origem[0]], 8-int(origem[1])
        d_col, d_lin = colunas[destino[0]], 8-int(destino[1])

        # Mover peça
        peca = board[o_lin][o_col]
        if peca == ".":
            print("Nenhuma peça na origem!")
            return False

        board[d_lin][d_col] = peca
        board[o_lin][o_col] = "."
        return True

    except Exception as e:
        print("Movimento inválido!", e)
        return False


# ------------------ Jogo -------------------

tabuleiro = criar_tabuleiro()
turno = "branco"

while True:
    mostrar_tabuleiro(tabuleiro)
    print(f"Turno: {turno}")

    origem = input("De: (ex: e2) ")
    destino = input("Para: (ex: e4) ")

    if mover(tabuleiro, origem, destino):
        turno = "preto" if turno == "branco" else "branco"
