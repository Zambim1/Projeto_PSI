from controller.cadastro_controller import cadastro_usuario
from database.criar_tabelas import criar_tabelas
import getpass
import socket
import config
from dao.tentativa_registro_dao import registrar_tentativa

def obter_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "127.0.0.1"

def obter_senha_com_asteriscos(prompt="Digite a senha: "):
    senha = getpass.getpass(prompt)
    return senha

def menu():
    while True:
        print("\nBem-vindo ao sistema de cadastro!")
        print("Digite 'sair' a qualquer momento para sair.")
        
        username = input("Digite o nome de usuário: ")
        if username.lower() == 'sair':
            print("Saindo...")
            break
        
        email = input("Digite seu e-mail: ")
        if email.lower() == 'sair':
            print("Saindo...")
            break
        
        ip = obter_ip()

        senha = obter_senha_com_asteriscos("Digite a senha: ")
        if senha.lower() == 'sair':
            print("Saindo...")
            break
        
        senha_confirmacao = obter_senha_com_asteriscos("Confirme a senha: ")
        if senha_confirmacao.lower() == 'sair':
            print("Saindo...")
            break

        while senha != senha_confirmacao:
            print("Erro: As senhas não coincidem. Tente novamente.")
            senha = obter_senha_com_asteriscos("Digite a senha: ")
            if senha.lower() == 'sair':
                print("Saindo...")
                break
            senha_confirmacao = obter_senha_com_asteriscos("Confirme a senha: ")
            if senha_confirmacao.lower() == 'sair':
                print("Saindo...")
                break

        if senha != senha_confirmacao:
            continue  

        permitido, tempo_restante = cadastro_usuario(ip, username, email, senha)
        
        if permitido:
            print("Cadastro realizado com sucesso!")
            break  
        else:
            print(tempo_restante)
            registrar_tentativa(ip, email, username)  

if __name__ == "__main__":
    try:
        criar_tabelas() 
        menu()  
    except Exception as e:
        print(f"Ocorreu um erro: {e}")