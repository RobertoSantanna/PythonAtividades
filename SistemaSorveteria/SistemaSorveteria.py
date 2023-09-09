print('Bem vindo a loja do Sr. Roberto Santana')
print('-------------------------------------CARDÁPIO--------------------------------------')
print('| N° DE BOLAS | SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |')
print('|      1      |       R$ 6,00          |      R$ 7,00       |       R$ 8,00       |')
print('|      2      |       R$ 11,00         |      R$ 13,00      |       R$ 15,00      |')
print('|      3      |       R$ 15,00         |      R$ 18,00      |       R$ 21,00      |')
print('-----------------------------------------------------------------------------------')

precos = {
    'tr': {1: 6, 2: 11, 3: 15},
    'pr': {1: 7, 2: 13, 3: 18},
    'es': {1: 8, 2: 15, 3: 21}
}
valorTotal = 0
while True:
    saborSorvete = input("Digite o sabor desejado (tr, pr ou es): ")
    if saborSorvete not in('tr', 'pr', 'es'):
        print("Sabor de sorvete inválido")
        continue

    quantidadeBolas = input("Digite a quantidade de bolas (1, 2, ou 3): ")

    if not quantidadeBolas.isdigit() or quantidadeBolas not in ['1', '2', '3']:
        print("Quantidade de bolas inválida. Insira o valor entre 1, 2 ou 3 bolas")
        continue

    quantidadeBolas = int(quantidadeBolas)

    preco = precos[saborSorvete][quantidadeBolas]
    valorTotal += preco
    print("Você escolheu {} bolas de sorvete no sabor {}: R${}".format(quantidadeBolas, saborSorvete, preco))

    sair = input("Deseja fazer outro pedido? (s/n): ")
    if sair.lower() != 's':
        break

print("O valor total ficou: R${}".format(valorTotal))