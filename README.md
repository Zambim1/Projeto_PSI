# Projeto_PSI

Este projeto tem como principal objetivo criar e implementar um código funcional que englobe as tecnologias de criptografia simétrica (AES), criptografia assimétrica (RSA), hashing de senhas (bcrypt) e autenticação com Tokens JWT (JSON Web Token), tendo em vista um contexto de um sistema de segurança da informação.

**Estrutura do Projeto**

O código do projeto está estruturado dentro do padrão DAO + MVC, apresentando a seguinte estrutura hierárquica:

---

## Script/

- **pycache**: Deveria agrupar todos os arquivos .pyc, porém parece não estar funcionando corretamente por causa da IDE. Precisa ser revisitado. De qualquer forma, essa pasta é ignorada pelo repositório, evitando carregar dados .pyc de outras máquinas.
  
---

- **controller/**:
  - `cadastro_controller.py`: Responsável por armazenar o fluxo de cadastro do usuário.
  - `login_controller.py`: Ainda vazio, mas receberá futuramente o fluxo para login.

---

- **dao/**:
  - `tentativa_registro_dao.py`: Responsável pela manipulação da tabela que comporta as tentativas de registro, também criando um bloqueio para tentativas subsequentes.
  - `usuario_dao.py`: Responsável pela manipulação da tabela que comporta as informações de usuário, sendo elas Nome, Email, hash da senha e o salt utilizado.

---

- **database/**:
  - `conectar.py`: Faz a conexão do banco de dados.
  - `criar_tabelas.py`: Cria as tabelas no banco de dados necessárias para o funcionamento do projeto.
  - `usuarios.db`: Essa pasta NÃO virá junto do repositório, ela será criada automaticamente na primeira execução do .py acima ou no começo de uma execução normal do projeto através da main.py

---

- **service/**:
  - `autenticacao_service.py`: Contém os componentes relacionados à criptografia do projeto.

---

- **config.py**: Contém as definições de variável ambiente, condensa a criação automática de .pycs na pasta pycache. Infelizmente não está funcionando ainda no ambiente de trabalho da IDE vs code.

---

- **main.py**: É o executável principal do projeto. Sempre que for iniciar uma execução normal do projeto, execute este arquivo.

---

Além dos componentes intrínsecos ao projeto, fora do diretório `script` possuímos diagram, docs e gitignore, sendo responsáveis por dividir, respectivamente, os diagramas, os documentos e as configurações que permitem o repositório ignorar o envio de arquivos indesejados.
