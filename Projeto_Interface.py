import sqlite3

# Funções CRUD
def criar_conexao():
    return sqlite3.connect('database/contatos.db')

def criar_tabela():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        endereco TEXT NOT NULL
    );
    """)
    conexao.commit()
    conexao.close()

def create_contact(nome, telefone, endereco):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO contatos (nome, telefone, endereco) VALUES (?, ?, ?);", (nome, telefone, endereco))
    conexao.commit()
    conexao.close()

def read_contacts():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contatos;")
    contatos = cursor.fetchall()
    for contato in contatos:
        print(contato)
    conexao.close()

def update_contact(id, nome, telefone, endereco):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("UPDATE contatos SET nome = ?, telefone = ?, endereco = ? WHERE id = ?;", (nome, telefone, endereco, id))
    conexao.commit()
    conexao.close()

def delete_contact(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?;", (id,))
    conexao.commit()
    conexao.close()

# Função do Menu
def menu():
    criar_tabela()
    while True:
        print("\n--- Menu CRUD CONTATOS ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Atualizar contato")
        print("4. Remover contato")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("Tela Criar Contato")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            create_contact(nome, telefone, endereco)
        elif escolha == '2':
            print("Tela Visualizar Contatos")
            read_contacts()
        elif escolha == '3':
            print("Tela Editar Contato")
            id = int(input("ID do contato: "))
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            endereco = input("Novo endereço: ")
            update_contact(id, nome, telefone, endereco)
        elif escolha == '4':
            id = int(input("ID do contato a remover: "))
            delete_contact(id)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
