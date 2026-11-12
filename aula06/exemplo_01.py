print('''
DESCONTOS: 

PIX: 12%
DÉBITO: 8%
CRÉDITO: 5%
DINHEIRO: 15% 

''')

desconto = 0


valor = float(input("Informe o valor: "))

opcao = int(input("Informe a opcao escolhida: "))

operacao = True

match opcao:
    case 1: 
        print("------PIX------")
        desconto = valor *0.12
        valor_final = valor - desconto
        print(f'O valor com desconto é: {valor_final}')

match opcao:
    case 2: 
        print("------débito------")
        desconto = valor *0.08
        valor_final = valor - desconto
        print(f'O valor com desconto é: {valor_final}')

match opcao:
    case 3: 
        print("------crédito------")
        desconto = valor *0.05
        valor_final = valor - desconto
        print(f'O valor com desconto é: {valor_final}')

match opcao:
    case 4: 
        print("------dinheiro------")
        desconto = valor *0.15
        valor_final = valor - desconto
        print(f'O valor com desconto é: {valor_final}')



if desconto != 0:
    valor_final = valor - desconto
    print(f'Preço: {valor}')
    print(f'desconto: {desconto}')
    print(f'Total a pagar: {valor_final}')

else:
    print("Escolha a opção correta")


if opcao in [1, 2, 3, 4]:

    valor_final = valor - desconto
    print(f" Preço: {valor}")
    print(f" Desconto: {desconto}")
    print(f" A pagar: {valor_final}")

else:
    print("Escolha uma opção válida.")