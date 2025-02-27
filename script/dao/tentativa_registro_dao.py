import sqlite3
from database.conectar import conectar

LIMITE_TENTATIVAS = 3
TEMPO_BLOQUEIO = 300

def verificar_tentativas(ip, email):
    conexao = conectar()
    cursor = conexao.cursor()

    # Verifica as tentativas baseadas no IP e Email combinados
    cursor.execute(""" 
    SELECT tentativas, strftime('%s', 'now') - strftime('%s', ultima_tentativa)
    FROM tentativa_registro
    WHERE ip = ? AND email = ?
    ORDER BY ultima_tentativa DESC
    LIMIT 1
    """, (ip, email))
    
    resultado = cursor.fetchone()
    conexao.close()

    # Se não houver resultado, significa que não há tentativas anteriores
    if resultado:
        tentativas, tempo_passado = resultado
        if tentativas >= LIMITE_TENTATIVAS and tempo_passado < TEMPO_BLOQUEIO:
            return False, TEMPO_BLOQUEIO - tempo_passado

    return True, 0

def registrar_tentativa(ip, email, username, sucesso=False):
    conexao = conectar()
    cursor = conexao.cursor()

    # Registra ou atualiza a tentativa de cadastro considerando o IP e Email
    cursor.execute("""
    SELECT id, tentativas FROM tentativa_registro WHERE ip = ? AND email = ?
    ORDER BY ultima_tentativa DESC LIMIT 1
    """, (ip, email))
    
    resultado = cursor.fetchone()

    if resultado:
        tentativa_id, tentativas = resultado
        if sucesso:
            # Se o cadastro foi bem-sucedido, zeramos as tentativas
            cursor.execute("UPDATE tentativa_registro SET tentativas = 0, ultima_tentativa = CURRENT_TIMESTAMP WHERE id = ?",
                           (tentativa_id,))
        else:
            # Caso contrário, incrementamos as tentativas
            cursor.execute("UPDATE tentativa_registro SET tentativas = ?, ultima_tentativa = CURRENT_TIMESTAMP WHERE id = ?",
                           (tentativas + 1, tentativa_id))
    else:
        # Se não existir uma tentativa anterior, inserimos uma nova tentativa
        if not sucesso:
            cursor.execute("""
            INSERT INTO tentativa_registro (ip, email, username, tentativas) 
            VALUES (?, ?, ?, 1)
            """, (ip, email, username))

    conexao.commit()
    conexao.close()