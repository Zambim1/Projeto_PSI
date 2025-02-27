from database.conectar import conectar

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL,
        salt TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tentativa_registro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT NOT NULL,
        email TEXT,
        username TEXT,
        tentativas INTEGER DEFAULT 1,
        ultima_tentativa TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conexao.commit()
    conexao.close()