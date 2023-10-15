# Importando o módulo sys para uso posterior
import sys

# Definindo variáveis globais para quantidade e total
total = 0

# Definindo o estoque inicial e pedido vazio
estoque = {
    'vinho 1: tinto': 10,
    'vinho 2: rosé': 15,
    'vinho 3: branco': 12,
    'vinho 4: frisante': 13,
    'rolhas': 50,
    'rótulos': 70,
    'embalagens': 30  # Adicionando embalagens ao estoque
}

def mostrarEstoque(estoque):
    print('----------- Estoque -----------')
    for item, quantidade in estoque.items():
        print(f'{item} - quantidade {quantidade}')

# Função para registrar entrada de itens no estoque
def registrarEntrada(estoque, item, quantidade):
    if item in estoque:
        estoque[item] += quantidade
        print(f"Entrada de {quantidade} {item} registrada!")
    else:
        print("Item não identificado.")

# Função para registrar saída de itens do estoque
def registrarSaida(estoque, item, quantidade):
    if item in estoque and estoque[item] >= quantidade:
        estoque[item] -= quantidade
        print(f"Saida de {quantidade} {item} registrada!")
    else:
        print("Estoque insuficiente.")

# Função para registrar entrada de itens no estoque
def registrarEntrada(estoque, vinho, quantidade):
    if vinho in estoque:
        estoque[vinho] += quantidade
        print(f"Entrada de {quantidade} {vinho} registrada!")
    else:
        print("Item não identificado.")

# Função para registrar saída de itens do estoque
def registrarSaida(estoque, vinho, quantidade):
    if vinho in estoque and estoque[vinho] >= quantidade:
        estoque[vinho] -= quantidade
        print(f"Saida de {quantidade} {vinho} registrada!")
    else:
        print("Estoque insuficiente.")

# Função para adicionar itens ao pedido
def adicionarPedido(pedido, estoque, vinho, quantidade, caixaOuGarrafa):
    if caixaOuGarrafa == 1:
        if vinho in estoque and estoque[vinho] >= quantidade:
            pedido[vinho] = pedido.get(vinho, 0) + quantidade
            print(f"{quantidade} {vinho} adicionado(s) ao pedido.")
        else:
            print("Item não identificado.")
    elif caixaOuGarrafa == 2:
        pedido[vinho] = pedido.get(vinho, 0) + quantidade * 6
        print(f"{quantidade} {vinho} adicionado(s) ao pedido.")

# Função para calcular o valor total do pedido
def valorTotalPedido(pedido, precos):
    total = 0
    precos = {'vinho 1: tinto': 90, 'vinho 2: rosé': 110.90, 'vinho 3: branco': 87.60, 'vinho 4: frisante': 99.90}
    for item, quantidade in pedido.items():
        if item in precos:
            total += quantidade * precos[item] 

# Função para calcular o valor do frete
def calcula_frete(pedido, total):
    quantidade = len(pedido)  # Usar o tamanho do pedido para calcular a quantidade de itens
    frete = total * 0.1 + quantidade * 10 + 10
    return frete


# Função principal do programa
def main():
    # Definindo o estoque inicial e pedido vazio
    estoque = {'vinho 1: tinto': 10, 'vinho 2: rosé': 15, 'vinho 3: branco': 12, 'vinho 4: frisante': 13, 'rolhas': 50, 'rótulos': 70}
    pedido = {}
    frete = calcula_frete(pedido, total)  # Calculando o frete inicial
    precos = {'vinho1': 90, 'vinho2': 110.90, 'vinho3': 87.60, 'vinho4': 99.90}
    caixaOuGarrafa = 0

    while True:
        try:
            # Apresentando o menu principal
            print('----------- MENU -----------')
            print('Bem vindo a Vinheria Agnello!')
            mainMenu = int(input('Você é cliente ou funcionário?\n1- Cliente\n2- Funcionário\n3- sair\nEscolha uma opção: '))
            
            # Utilizando o switch-like "match" para lidar com as escolhas do menu
            match mainMenu:
                case 1:  # Menu do cliente
                    while True:
                        try:
                            print('----------- MENU -----------')
                            clienteMenu = int(input('Faça seu pedido!\n1- Adicionar vinho ao pedido\n2- Finalizar pedido\n3- Voltar\nEscolha uma opção: '))
                            
                            # Utilizando "match" para o menu do cliente
                            match clienteMenu:
                                case 1:  # Adicionar vinho ao pedido
                                    try:
                                        print('Escolha se deseja comprar garrafas ou caixas')
                                        while True:
                                            caixaOuGarrafa = int(input('1- Garrafas\n2- Caixas\nEscolha uma opção: '))
                                            if caixaOuGarrafa == 1 or caixaOuGarrafa == 2:
                                                for vinho, quantidade in estoque.items():
                                                    print(f'{vinho} - quantidade {quantidade}')
                                                vinho = input("Informe o vinho desejado: (escreva exatamente como está no menu)")
                                                quantidade = int(input("Informe a quantidade desejada: "))
                                                adicionarPedido(pedido, estoque, vinho, quantidade, caixaOuGarrafa)
                                                break
                                            else: 
                                                print('Digite uma opção válida.')
                                    except ValueError:
                                        print('Opção inválida')    
                                
                                case 2:  # Finalizar pedido
                                    subtotalPedido = valorTotalPedido(pedido, precos)
                                    calcula_frete(pedido, total)
                                    print('Resumo do seu pedido:')
                                    for vinho, quantidade in pedido.items():
                                        print(f'{vinho} - {quantidade}')
                                    print(f'O subtotal do seu pedido é de: {subtotalPedido} e seu frete é {frete}')
                                    exit()                            

                                case 3:  # Voltar
                                    break 
                                
                                case other:  # Opção inválida
                                    print('Digite uma opção válida') 
                        
                        except ValueError:
                            print('Opção inválida')
                
                case 2:  # Menu do funcionário
                    while True:
                        try:
                            print('----------- MENU -----------')
                            funcionarioMenu = int(input('1- Registrar entrada\n2- Registrar saída\n3- Verificar estoque\n4- Voltar\nEscolha uma opção: '))

                            if funcionarioMenu == 1:
                                print(estoque)
                                item = input("Informe o item que deseja registrar a entrada:  ")
                                quantidade = int(input("Informe a quantidade: "))
                                registrarEntrada(estoque, item, quantidade)
                            elif funcionarioMenu == 2:
                                print(estoque)
                                item = input("Informe o item que deseja registrar a saída: ")
                                quantidade = int(input("Informe a quantidade: "))
                                registrarSaida(estoque, item, quantidade)
                            elif funcionarioMenu == 3:
                                mostrarEstoque(estoque)
                            elif funcionarioMenu == 4:
                                break
                            else:
                                print('Opção inválida')
                        except ValueError:
                            print('Opção inválida')
                            
                        except ValueError:
                            print('Opção inválida')
                        break
                
                case 3:  # Sair do programa
                    break  
                
                case other:  # Opção inválida
                    print('Digite uma opção válida') 
        except ValueError:
            print('Opção inválida')

# Chamando a função principal para iniciar o programa
main()


meu_dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}

numero_de_itens = len(meu_dicionario)
print("Número de itens no dicionário:", numero_de_itens)