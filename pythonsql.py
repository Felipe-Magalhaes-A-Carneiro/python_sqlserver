import pyodbc

# Conexão com o SQL Server:
connection_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=ALUNO02\SQLEXPRESS;"
    "DATABASE=Python;"
    "UID=Teste2;"
    "PWD=teste2;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(connection_str)
cursor = conn.cursor()

print("""
        ____________________________________________________
        |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
        |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
        ----------------------------------------------------

Seja bem-vindo(a).
Cadastre livros no nosso Banco de Dados, no SQL Server. 

>>> Utilizaremos o método CRUD - CREATE(CRIAR), READ(LER), UPDATE(ATUALIZAR) e DELETE(DELETAR).

ATENÇÃO: Siga as instruções em cada MENU que disponibilizarmos.
""")

iniciar = input("\n>>> Digite 'y' para começar ou outro digito para sair do programa: ")

# USO DO CRUD:

# 1 - CREATE - Criar / Inserir valores:

def create():
    print("\n------ CRIANDO REGISTROS ------\n")
    titulo = input("Digite o titulo do livro: ").title()
    autor = input("Digite o autor do livro: ").title()
    ano = input("Digite o ano do livro: ")


    string_sql = f"""
        INSERT INTO Livros (titulo, autor, ano) VALUES
        (?, ?, ?);

    """
    # 1.2 - Retorna os valores com os dados inseridos pelo usuário e entrega-os junto com a sgring_sql por 'placeholders':

    dados = (titulo, autor, ano)
    cursor.execute(string_sql, dados)
    conn.commit()

# 2 - READ - Ler valores cadastrados no banco de dados:

def read():
    read_sql = "SELECT * FROM Livros;"
    cursor.execute(read_sql)
    todos_registros = cursor.fetchall()

    print("\n------ REGISTRO DE LANÇAMENTOS ------\n")
    for registro in todos_registros:
        print(registro)

# 2.1 - Filtar dados específicos:

def querry_unico():
    print("\n------ PESQUISA PERSONALIZADA ------\n")
    escolha = input("""               
        Digite o número de uma das opções abaixo:
              
    1- Pesquisar pelo TÍTULO do Livro;
    2- Pesquisar pelo AUTOR;
    3- Pesquisar pelo ANO;

                    """)

    if escolha == "1":
        querry_titulo = input("Digite o titulo do livro que procura: ")
        read_sql = "SELECT * FROM Livros WHERE titulo = ?"
        cursor.execute(read_sql, (querry_titulo))
        registro = cursor.fetchall()
        print(registro)

    if escolha == "2":
        querry_autor = input("Digite o autor do livro que procura: ")
        read_sql = "SELECT * FROM Livros WHERE autor = ?"
        cursor.execute(read_sql, (querry_autor))
        registro = cursor.fetchall()
        print(registro)

    if escolha == "3":
        querry_ano = input("Digite o ano do livro que procura: ")
        read_sql = "SELECT * FROM Livros WHERE ano = ?"
        cursor.execute(read_sql, (querry_ano))
        registro = cursor.fetchall()
        print(registro)

    if escolha == "0":
        read()
    return

# 3 - UPDATE - Atualizar dados já registrados:
def update():
    print("\n------ ATUALIZANDO DADOS ------\n")
    id_livro = input("Atualizando Título do Lívro - Digite o ID do lívro que deseja modificar: ")
    update_titulo = input("Atualizando Título do Lívro- Digite o NOVO Título do lívro: ")
    update_autor = input("Atualizando Título do Lívro- Digite o NOVO Autor do lívro: ")
    update_ano = input("Atualizando Título do Lívro- Digite o NOVO Ano do lívro: ")

    update_sql = "UPDATE Livros SET titulo = ?, autor = ?, ano = ? WHERE id = ?"
    cursor.execute(update_sql, (update_titulo, update_autor, update_ano, id_livro))

    conn.commit()
    read()

# 4 - DELETE - Deletar dados
def delete():
    print("\n------ DELETANDO DADOS ------\n")
    read()
    deletar_id = input("DELETAR Registro de Livros - Digite o ID do livro que deseja DELETAR: ")
    delete_sql = "DELETE FROM Livros WHERE titulo = ?"
    cursor.execute(delete_sql, (deletar_id, ))
    conn.commit()

def main():
    while True:
        print("""

        >>> MENU PRINCIPAL
            Digite o número de uma das opções abaixo:
              
        1- Criar novos registros de Livros;
        2- Visualizar registros de Livros já cadastrados;
        3- Pesquisa personalizada de Livros já cadastrados;
        4- Atualizar registros de Livros já cadastrados;
        5- Deletar registros de Livros já cadastrados;
        
        0- Sair do sistema.

        """)

        escolha = input("\n>>> Digite a sua escolha: ")

        if escolha == "1":
            create()
        elif escolha == "2":
            read()
        elif escolha == "3":
            querry_unico()
        elif escolha == "4":
            update()
        elif escolha == "5":
            delete()
        elif escolha == "0":
            print("\n*** Saindo do programa... ***")
            print("""
                ____________________________________________________
                |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
                |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
                ----------------------------------------------------
                
            ### Obrigado por utilizar o nosso programa. Volte sempre! ###\n""")
            break
        else:
            print("Digite uma das opções válidas")

if iniciar == 'y':
    main()
else:
    print("\n### Saindo do programa... ###")
    print("""
        ____________________________________________________
        |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
        |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
        ----------------------------------------------------
          
    ### Obrigado por utilizar o nosso programa. Volte sempre! ###\n""")
    exit()

conn.close()
