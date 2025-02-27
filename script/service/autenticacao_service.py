import bcrypt

def criptografar_senha(senha, salt):
    return bcrypt.hashpw(senha.encode(), salt)

def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode(), senha_hash)