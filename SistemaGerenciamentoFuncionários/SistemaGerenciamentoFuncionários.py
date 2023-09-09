lista_colaboradores = [] #lista para armazenar os colaboradores.
id_global = 0 #variável global para rastrear o ID dos colaboradores.

def cadastrar_colaborador(id): #Função para cadastrar um novo colaborador.

    nome = input("Insira o nome do Colaborador: ") #Solicita informações do colaborador.
    setor = input("Insira o setor do Colaborador: ")
    salario = float(input("Insira o salário do Colaborador: "))
    lista_colaboradores.append({"ID": id, "Nome": nome, "Setor": setor, "Salário": salario}) #dicionário representando o colaborador e o adiciona na lista de colaboradores.
    print(f"Colaborador cadastrado com sucesso (ID: {id})")


def consultar_colaborador(): #Função para consultar informações sobre os colaboradores.
    if not lista_colaboradores: #Se não existir colaboradores cadastrados.
        print("Nenhum colaborador cadastrado.")
        return
    #para escolher o tipo de consulta
    print("\nEscolha o tipo de consulta: \n1: Consultar todos\n2: Consultar por ID\n 3: Consultar por Setor\n4: Retornar ao menu  ") #Para 

    opcao = input("Escolha uma opção: ")

    if opcao == "1": #Se escolher 1 referente a consultar os colaboradores cadastrados.
        for i, colaborador in enumerate(lista_colaboradores, 1):
            print(f"ID: {i}, Nome: {colaborador['Nome']}, Setor: {colaborador['Setor']}, Salário: R${colaborador['Salário']:.2f}")
    elif opcao == "2": #se escolher 2 referente a consultar um colaborador por id
        id_busca = int(input("Digite o ID do colaborador: ")) - 1 
        if 0 <= id_busca < len(lista_colaboradores): #verificar se o id inserido é válido.
            colaborador = lista_colaboradores[id_busca]
            print(f"Nome: {colaborador['Nome']}, Setor: {colaborador['Setor']}, Salário: R${colaborador['Salário']:.2f}")
        else:
            print("ID inválido.") #se o id for inválido
    elif opcao == "3": #se escolher 3 referente a consultar colaboradores por setor
        setor_busca = input("Digite o setor a ser consultado: ")
        encontrados = [colaborador for colaborador in lista_colaboradores if colaborador['Setor'].lower() == setor_busca.lower()]
        if encontrados: #se encontrar colaboradores no setor inserido
            for i, colaborador in enumerate(encontrados, 1): 
                print(f"ID: {i}, Nome: {colaborador['Nome']}, Setor: {colaborador['Setor']}, Salário: R${colaborador['Salário']:.2f}")
        else: #se não encontrar nenhum colaborador do setor inserido
            print("Nenhum colaborador encontrado neste setor.")
    else: #se inserir algum valor inválido
        print("Opção inválida.")

def remover_colaborador():
    if not lista_colaboradores: #se não tiver nenhum colaborador cadastrado
        print("Nenhum colaborador cadastrado.")
        return

    print("\nColaboradores cadastrados:") #lista os colaboradores e permite remover um colaborador por id
    for i, colaborador in enumerate(lista_colaboradores, 1):
        print(f"ID: {i}, Nome: {colaborador['Nome']}")

    id_remover = int(input("Digite o ID do colaborador a ser removido: ")) - 1 #Para remover colaborador

    if 0 <= id_remover < len(lista_colaboradores):
        removido = lista_colaboradores.pop(id_remover) #remove o colaborador da lista
        print(f"Colaborador '{removido['Nome']}' removido com sucesso") 
    else: #se o id for invalido
        print("Tipo de ID inválido.")

def main(): #função principal do programa
    global id_global
    print("Bem-vindo ao sistema de gerenciamento do Sr. Roberto Santana") #Mensagem de boas vindas

    while True: #loop principal do menu
        print("\nMenu:")
        print("1. Cadastrar Colaborador")
        print("2. Consultar Colaborador")
        print("3. Remover Colaborador")
        print("4. Encerrar Programa")

        opcao_menu = input("Escolha uma opção: ")

        if opcao_menu == "1": #se escolher 1 referente a cadastrar um novo colaborador
            id_global += 1
            cadastrar_colaborador(id_global)
        elif opcao_menu == "2":#se escolher 2 referente a consultar informações de um colaborador
            consultar_colaborador()
        elif opcao_menu == "3":#se escolher 3 referente a remover um colaborador
            remover_colaborador()
        elif opcao_menu == "4":#se escolher 4 referente a encerrar o programa
            print("Encerrando o programa.")
            break
        else: #se inserir algum dado que não for referente ao menu (1, 2, 3 ou 4)
            print("Opção inválida..")

if __name__ == "__main__": #chama a função principal main quando o programa for executado
    main()