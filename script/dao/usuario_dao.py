import sqlite3
from database.conectar import conectar

def verificar_usuario_existente(username, email):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM usuarios WHERE username = ? OR email = ?", (username, email))
    resultado = cursor.fetchone()

    conexao.close()
    return resultado is not None

def salvar_usuario(username, email, senha_hash, salt):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO usuarios (username, email, senha_hash, salt) VALUES (?, ?, ?, ?)", 
                   (username, email, senha_hash, salt))

    conexao.commit()
    conexao.close()

def buscar_usuario_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    resultado = cursor.fetchone()

    conexao.close()
    return resultado