print("ENTRAR")
email_cadastrado = "devgabriel@gmail.com"
senha_cadastrada = 1392813

while True:
    email_login = input("\nDigite o email: ")

    if email_login != email_cadastrado:
        print("Email incorreto!")
        continue

    while True:
        senha_login = int(input("\nDigite a senha: "))

        if senha_login != senha_cadastrada:
            print("Senha incorreta!")
            continue

        print("Login realizado com sucesso!")
        break

    break
