from src.service.service_user import ServiceUser


def main():
    service = ServiceUser()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar usuário")
        print("2 - Remover usuário")
        print("3 - Exibir todos usuários")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            name = input("Digite o nome do usuário: ")
            job = input("Digite o Job do usuário: ")
            resultado = service.add_user(name, job)
            print(resultado)

        elif opcao == "2":
            name = input("Digite o nome do usuário para remover: ")
            resultado = service.remove_user(name)
            print(resultado)

        elif opcao == "3":
            if service.store.bd:
                print("\nLista de usuários:")
                for i, user in enumerate(service.store.bd, start=1):
                    print(f"{i}. Nome: {user.name}, Job: {user.job}")
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "4":
            print("Sua sessão foi encerrada.")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()