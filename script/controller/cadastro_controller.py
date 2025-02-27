from dao.usuario_dao import verificar_usuario_existente, salvar_usuario
from dao.tentativa_registro_dao import verificar_tentativas, registrar_tentativa
from service.autenticacao_service import criptografar_senha
import bcrypt

def cadastro_usuario(ip, username, email, senha):
    registrar_tentativa(ip, email, username)

    permitido, tempo_restante = verificar_tentativas(ip, email)
    if not permitido:
        return False, f"Cadastro bloqueado. Tente novamente em {int(tempo_restante)} segundos."

    if verificar_usuario_existente(username, email):
        return False, "Erro: Nome de usuário ou e-mail já cadastrados."

    salt = bcrypt.gensalt()
    senha_hash = criptografar_senha(senha, salt)

    salvar_usuario(username, email, senha_hash, salt)
    return True, "Usuário cadastrado com sucesso!"