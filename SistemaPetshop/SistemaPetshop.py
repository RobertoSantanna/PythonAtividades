print('Bem vindo a loja do Sr. Roberto Santana') #Mensagem de boas vindas

def cachorro_peso(): #Definindo a primeira função.
    while True: #Enquanto for verdadeiro;
        try:
            peso = float(input("Insira o peso do cachorro (kg): ")) #Entre com o peso do cachorro.
            if peso < 3: #Se o peso do cachorro for menor do que 3 kg:
                return 40 #O valor cobrado será 40 reais
            elif 3 <= peso < 10: #Se o peso do cachorro for maior do que 3 e menor do que 10 kg:
                return 50 #O valor cobrado será 50 reais
            elif 10 <= peso < 30: #Se o peso do cachorro for maior do que 10 e menor do que 30 kg:
                return 60 #O valor cobrado será 60 reais
            elif 30 <= peso < 50: #Se o peso do cachorro for maior do que 30 e menor do que 50 kg:
                return 70 #O valor cobrado será 70 reais
            else:
                print("Peso do cachorro acima do permitido!") #Caso o peso do cachorro exceda 50 kg, mostrar esta mensagem!
        except ValueError: #Caso seja adicionado um caractér que não seja um número, as mensagens a seguir irão aparecer:
            print("Você digitou um valor não numérico.")
            print('Por gentileza insira o peso correto do cachorro.')

def cachorro_pelo(): #Definindo a segunda função.
    while True: #Enquanto for verdadeiro:
        pelo = input("Insira o tipo de pelo do cachorro: \nDigite:\n c - Para cachorros com pelo curto \n m - Para cachorros com pelo médio \n l - Para cachorros com pelo longo ")
        if pelo in['c', 'm', 'l']:
            if pelo == 'c': #Se escolher o c referente ao pelo curto:
                return 1 #Valor multiplicador será 1
            elif pelo == 'm': #Se escolher o c referente ao pelo médio:
                return 1.5 #Valor multiplicador será 1.5
            elif pelo == 'l': #Se escolher o c referente ao pelo longo:
                return 2 #Valor multiplicador será 2
        else:
            print("Tipo de pelo inválido!") #Caso o cliente digite algum caracter que não seja: c, m e l, esta mensagem aparecerá!

def cachorro_extra(): #Definindo a terceira função.
    extra = 0
    while True: #Enquanto o cliente escolher os serviços adicionais, continuar pergutando se ele irá querer mais algum.
        try:
            adicional = int(input("Escolha o serviço adicional \nDigite:\n 1 - Cortar as unhas \n 2 - Escovar os dentes \n 3 - Limpar as orelhas \n 0 - Não quero serviços adicionais"))
            if adicional == 0: #Se o cliente não quiser adicionar serviços
                return extra #O valor cobrado a mais será 0
            elif adicional == 1: #Se o cliente quiser adicionar o corte de unhas.
                extra += 10 #O valor adicional será 10 reais.
                print("Serviço adicional escolhido: Corte de unhas - R$ 10, 00") #Aparecer está mensagem caso o cliente adicionar o corte de unhas!
            elif adicional == 2: #Se o cliente quiser adicionar a escovação de dentes.
                extra += 12 #O valor adicional será 12 reais.
                print("Serviço adicional escolhido: Escovar dentes - R$ 12, 00") #Aparecer está mensagem caso o cliente adicionar a escovação de dentes!
            elif adicional == 3: #Se o cliente quiser adicionar o serviço de limpeza de olhas.
                extra += 15 #O valor adicional será 15 reais.
                print("Serviço adicional escolhido: Limpar orelhas - R$ 15, 00") #Aparecer está mensagem caso o cliente queira adicionar a limpeza de oreolhas!
            else:
                print("Valor adicional inválido!") #Caso o cliente digite um valor que não seja 1, 2, 3 e 4.
        except valueError:
            print("Valor de serviço inválido!") #Caso o cliente digite um valor que não seja 1, 2, 3 e 4.

def main():
    peso = cachorro_peso() #Função cachorro_peso atribuída a peso
    multiplicador = cachorro_pelo() #Função cachorro_pelo atribuído ao multiplicador
    servico_extra = cachorro_extra() #Função cachorro_extra atribuído ao servico_extra

    total = peso * multiplicador + servico_extra #Valor total será o peso do cachorro * o multiplicador que é o tamanho do pelo + os serviços adicionais.

    # Imprimir o total a pagar com a sequência desejada
    print("Total a pagar (R$): {:.2f} (peso: {} * pelo: {} + adicionais: {:.2f})".format(total, peso, multiplicador, servico_extra))

if __name__ == "__main__":
    main()