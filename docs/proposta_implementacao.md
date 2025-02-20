Cadastro de usuário – Hash de senha com bcrypt
Tecnologia usada: bcrypt
Objetivo: Proteger as senhas dos usuários contra ataques, garantindo que não sejam armazenadas em formato legível.
Etapas de implementação:
1. O usuário preenche o formulário de cadastro com nome, e-mail e senha.
2. Antes de salvar a senha no banco de dados, o sistema gera um hash seguro usando bcrypt.
bcrypt adiciona um salt (valor aleatório) para tornar cada hash único, dificultando ataques de força bruta.
3. O hash resultante é armazenado no banco de dados junto com os demais dados do usuário.
4. A senha original nunca é armazenada, garantindo maior segurança.

Login – Geração e verificação de Token JWT
Tecnologia usada: JWT (JSON Web Token)
Objetivo: Autenticar o usuário e permitir acesso seguro às funcionalidades do sistema sem precisar armazenar sessões no servidor.
Etapas de implementação:
1. O usuário insere e-mail e senha no login.
2. O sistema busca o usuário no banco de dados e recupera o hash da senha.
3. Com bcrypt.compare(), verifica se a senha digitada corresponde ao hash salvo.
4. Se estiver correta, o sistema gera um Token JWT, contendo informações como ID do usuário e permissões.
O token é assinado com uma chave secreta, garantindo que não possa ser falsificado.
5. O token é enviado ao usuário e armazenado no localStorage ou cookies seguros.
6. Nas próximas requisições, o sistema verifica o token antes de permitir o acesso às funcionalidades protegidas.

Criptografia de mensagens – Uso de AES (CBC)
Tecnologia usada: AES (Advanced Encryption Standard) – Modo CBC (Cipher Block Chaining)
Objetivo: Garantir que as mensagens armazenadas no sistema não possam ser lidas por terceiros sem autorização.
Etapas de implementação:
1. O usuário digita a mensagem e a envia.
2. O sistema gera uma chave AES exclusiva para criptografar a mensagem.
3. A mensagem é criptografada usando o algoritmo AES no modo CBC, que aumenta a segurança ao usar um vetor de inicialização (IV) aleatório para cada mensagem.
4. O resultado da criptografia (ciphertext) é armazenado no banco de dados.
5. A chave AES usada para criptografia não é armazenada diretamente, pois será protegida usando RSA

Proteção da chave AES – Uso de RSA para criptografar a chave antes de armazená-la
Tecnologia usada: RSA (Rivest-Shamir-Adleman)
Objetivo: Proteger a chave AES, garantindo que apenas o destinatário correto consiga descriptografar a mensagem.
Etapas de implementação:
1. Cada usuário possui um par de chaves RSA (chave pública e chave privada).
2. Antes de salvar a mensagem no banco de dados, a chave AES é criptografada usando a chave pública RSA do destinatário.
3. Apenas o destinatário poderá descriptografar a chave AES usando sua chave privada RSA.
4. Quando o destinatário acessa a mensagem:
O sistema usa sua chave privada RSA para recuperar a chave AES.
Em seguida, a chave AES é usada para descriptografar a mensagem original.

Armazenamento seguro de dados
Para garantir a segurança dos dados armazenados, o sistema seguirá boas práticas, como:
Banco de dados seguro:
Hash de senhas em vez de armazenar senhas em texto puro.
Mensagens criptografadas antes de serem armazenadas.
Chaves AES protegidas com RSA.
Proteção de chaves:
As chaves privadas RSA nunca são armazenadas no banco de dados, apenas no dispositivo do usuário ou em um cofre seguro.
A chave secreta do JWT deve ser armazenada em variáveis de ambiente para evitar vazamentos.
Conexões seguras:
Todas as comunicações entre cliente e servidor devem usar HTTPS para evitar interceptação de dados.


