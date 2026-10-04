# Sistema de Login Escolar

print("================================")
print("       SISTEMA ESCOLAR")
print("================================")

# Cadastro
print("\n--- CADASTRO ---")

login = input("Crie seu login: ")
senha = input("Crie sua senha: ")

# Descobrindo se é aluno ou professor
if login.startswith("aluno_"):
    tipo = "Aluno"

elif login.startswith("prof_"):
    tipo = "Professor"

else:
    tipo = "Indefinido"

# Verificando se o login é válido
if tipo == "Indefinido":
    print("\nLogin inválido!")
    print("Alunos devem começar o login com: aluno_")
    print("Professores devem começar o login com: prof_")

else:
    print("\nCadastro realizado com sucesso!")
    print("Tipo de usuário:", tipo)

    # Login
    print("\n--- LOGIN ---")

    login_digitado = input("Digite seu login: ")
    senha_digitada = input("Digite sua senha: ")

    if login_digitado == login and senha_digitada == senha:
        print("\nLogin realizado com sucesso!")
        print("Usuário:", login_digitado)
        print("Você é:", tipo)

    else:
        print("\nLogin ou senha incorretos!")