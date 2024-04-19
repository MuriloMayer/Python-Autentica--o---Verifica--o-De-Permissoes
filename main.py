# Murilo Mayer Van Nouhuys
from getpass import getpass

while True:
    def verify_password (emailInpt, passwordInpt):
        with open('users.txt', 'r', encoding='utf-8') as file:
            users = file.readlines()
        for user in users:
            email, senha = user.strip().split(';')
            if email == emailInpt and senha == passwordInpt:
                return True
        return False

    def read_filetxt():
        with open('perm.txt', 'r', encoding='utf-8') as file:
            files = file.readlines()
            return files




    print("--------------------")
    print("Qual Ação Você Deseja Realizar? \n 1. Login \n 2. Criar Conta \n 3. Sair")
    print("--------------------")
    inputPrincipal = input(":")

    if inputPrincipal == "1":
        print("--------------------")
        print("Bem Vindo! Preencha Suas Credencias Para Efetuar o Login")
        print("--------------------")
        inputEmail = input("Digite seu Email: ")
        inputPassword = getpass("Digite Sua Senha:")
        print("--------------------")

        if verify_password(inputEmail, inputPassword):
            print("Login Realizado Com Sucesso!")
            print("--------------------\n")
            print("Bem Vindo! " + inputEmail + "\nComandos Disponíveis: \n 1. Verificar Arquivos \n 2. Ler Arquivo \n 3. Alterar Arquivo \n 4. Executar Arquivo \n 5. Sair")
            input_commands = input("Digite uma opção:")

            if input_commands == "1":
                files = read_filetxt()

                for file in files:
                    name = file.strip().split(';')
                    print(name[0])

            elif input_commands == "2":
                input_file = input("Digite o nome do arquivo: ")

                files = read_filetxt()

                for file in files:
                    user, name, read, write, execute = file.strip().split(';')
                    if user == inputEmail:
                        if name == input_file:
                            if read == "1":
                                print("Permissão Concedida!")
                            else:
                                print("Permissão Negada!")
                                break
            elif input_commands == "3":
                input_file = input("Digite o nome do arquivo: ")

                files = read_filetxt()

                for file in files:
                    user, name, read, write, execute = file.strip().split(';')
                    if user == inputEmail:
                        if name == input_file:
                            if write == "1":
                                print("Permissão Concedida!")
                            else:
                                print("Permissão Negada!")
                                break

            elif input_commands == "4":
                input_file = input("Digite o nome do arquivo: ")

                files = read_filetxt()

                for file in files:
                    user, name, read, write, execute = file.strip().split(';')
                    if user == inputEmail:
                        if name == input_file:
                            if execute == "1":
                                print("Permissão Concedida!")
                            else:
                                print("Permissão Negada!")
                                
                                
            elif input_commands == "5":
                print("Saindo...")
                exit()        
            else:
                print("Opção Inválida")
                break
            

        else:
            print("Email ou Senha Incorretos")
            break

    elif inputPrincipal == "2":
        print("Criar Conta (not working)")
        
    elif inputPrincipal == "3":
        print("Saindo...")
        exit()

    else:
        print("Opção Inválida")
        break