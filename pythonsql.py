import pyodbc


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

cursor.execute("SELECT * FROM Livros;")

for row in cursor.fetchall():
    print(row)


titulo = input("Digite o titulo do livro: ")
autor = input("Digite o autor do livro: ")
ano = input("Digite o ano do livro: ")

# Inserir valores:
string_sql = f"""
    INSERT INTO Livros (titulo, autor, ano) VALUES
    (?, ?, ?);

"""
dados = (titulo, autor, ano)

cursor.execute(string_sql, dados)
cursor.execute("SELECT * FROM Livros;")

conn.commit()

conn.close()
