import sqlite3

conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

# Criando a tabela
cursos.execute("""
    CREATE TABLE Vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendedor TEXT,
        produto TEXT,
        quantidade INTEGER,
        valor REAL
    )
""")

# Função para atualizar uma venda
def atualizar(id_venda, vendedor=None, produto=None, quantidade=None, valor=None):

    cursos.execute("""
        UPDATE Vendas
        SET vendedor = ?,
            produto = ?,
            quantidade = ?,
            valor = ?
        WHERE id = ?
    """, (vendedor, produto, quantidade, valor, id_venda))

    conn.commit()

# Menu
print("--- SISTEMA DE GERENCIAMENTO ---")
print("1. Adicionar material (C)")
print("2. Ver lista de materiais (R)")
print("3. Alterar material (U)")
print("4. Deletar material (D)")

escolha = input("Escolha a operação: ")

# CREATE
if escolha == "1":

    vendedor = input("Vendedor: ")
    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor: "))

    cursos.execute("""
        INSERT INTO Vendas (vendedor, produto, quantidade, valor)
        VALUES (?, ?, ?, ?)
    """, (vendedor, produto, quantidade, valor))

    conn.commit()

# READ
elif escolha == "2":

    cursos.execute("SELECT * FROM Vendas")

    for venda in cursos.fetchall():
        print(venda)

# UPDATE
elif escolha == "3":

    id_venda = int(input("Digite o ID da venda: "))
    vendedor = input("Novo vendedor: ")
    produto = input("Novo produto: ")
    quantidade = int(input("Nova quantidade: "))
    valor = float(input("Novo valor: "))

    atualizar(
        id_venda,
        vendedor,
        produto,
        quantidade,
        valor
    )

    print("Venda atualizada!")

# DELETE
elif escolha == "4":

    id_venda = int(input("Digite o ID para deletar: "))

    cursos.execute(
        "DELETE FROM Vendas WHERE id = ?",
        (id_venda,)
    )

    conn.commit()

    print("Venda deletada!")

else:
    print("Opção inválida.")

# Mostrar resultado
cursos.execute("SELECT * FROM Vendas")
print(cursos.fetchall())

conn.close()