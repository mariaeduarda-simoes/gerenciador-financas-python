from datetime import date

movimentacoes = []


def mostrar_menu():
    print("\n=== Gerenciador de Finanças ===")
    print("1 - Adicionar movimentação")
    print("2 - Listar movimentações")
    print("3 - Ver saldo")
    print("4 - Ver total por categoria")
    print("0 - Sair")


def adicionar():
    print("\n--- Nova movimentação ---")

    tipo = input("Tipo (1 = receita, 2 = despesa): ")
    if tipo == "1":
        tipo = "receita"
    elif tipo == "2":
        tipo = "despesa"
    else:
        print("Tipo inválido.")
        return

    try:
        valor = float(input("Valor: ").replace(",", "."))
    except ValueError:
        print("Valor inválido. Digite apenas números.")
        return

    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return

    categoria = input("Categoria (ex: alimentação, transporte): ").strip().lower()
    descricao = input("Descrição: ").strip()

    movimentacao = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
        "data": str(date.today()),
    }

    movimentacoes.append(movimentacao)
    print("Movimentação adicionada!")


def listar():
    print("\n--- Movimentações ---")

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação cadastrada ainda.")
        return

    for i, mov in enumerate(movimentacoes, start=1):
        sinal = "+" if mov["tipo"] == "receita" else "-"
        print(
            f"{i}. {mov['data']} | {mov['categoria']} | "
            f"{mov['descricao']} | {sinal} R$ {mov['valor']:.2f}"
        )


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saldo: em construção")
    elif opcao == "4":
        print("Categorias: em construção")
    elif opcao == "0":
        print("Até mais!")
        break
    else:
        print("Opção inválida, tente de novo.")