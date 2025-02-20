**Objetivo do projeto** = Segurança na informações entre funcionarios
**Tecnologias utilizadas** 
1. bcrypt = Hashing seguro de senhas, versão 5.5.0, utilizando a versão assincrona para que o servidor utilize o EventLoop e threads. 
2. PyJWT =  versão 2.10.1 ,Autenticação via Tokens JWT.
3. cryptography → Implementação de AES e RSA.

4. **Fluxo basico dos sistemas**
5. 1. **usuario faz cadastro** = usuario entra no sistema faz o seu cadastro com as normas e regras do sistema, salva no banco de dados.
   2. **usuario faz login** = usuario entra no sistema e faz o login exatamente como crio o cadastro no banco de dados.
   3. **Usuário envia uma mensagem criptografada com AES** =  é um protocolo de encriptação amplamente utilizado, projetado para proteger 
    dados sensíveis transformando informações legíveis num formato seguro e codificado.
    4.**Apenas o destinatário correto pode descriptografar com sua chave RSA** =  cria e depois publica o produto de dois números primos 
    grandes, junto com um valor auxiliar, como sua chave pública
      


   
