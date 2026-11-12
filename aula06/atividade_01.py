ingresso = float(input("Digite o valor do ingresso: "))

print('''


Digite o código de acordo com o tipo de entrada: 

[1] Inteira - Sem Desconto
[2] Meia - 50% de desconto
[3] Promoção - 30% de descnto

''')
tipo_de_entrada = int(input("Digite o código: "))

match tipo_de_entrada:

    case 1:
        print(f'Valor sem desconto, portanto, segue o valor da inteira de: {ingresso}')

    case 2:
        desconto = ingresso * 0.50
        final = ingresso - desconto
        print(final)

    case 3:
        desconto = ingresso * 0.30
        final = ingresso - desconto
        print(final)

    case _:
        print("Digite uma opção válida!")


       



