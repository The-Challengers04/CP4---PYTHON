#Gabriel Machado Belardino - RM550121
#Ana Beatriz Farah Alvez - RM97865
#Kaiky Alvaro de Miranda - RM98118
#Lucas Rodrigues da Silva - RM98344
#Pedro Henrique Bicas Couto - RM99534

quantidade = 0
def registrarEntrada(estoque, vinho, quantidade):
    if vinho in estoque:
        estoque[vinho] += quantidade
        print(f"Entrada de {quantidade} {vinho} registrada!")
    else:
        print("Item não identificado.")

def registrarSaida(estoque, vinho, quantidade):
    if vinho in estoque and estoque[vinho] >= quantidade:
        estoque[vinho] -= quantidade
        print(f"Saida de {quantidade} {vinho} registrada!")
    else:
        print("Estoque insuficiente.")
        
def adicionarPedido(pedido, vinho, quantidade, caixaOuGarrafa):
    if caixaOuGarrafa == 1:
        pedido[vinho] = pedido.get(vinho, 0) + quantidade
        print(f"{quantidade} {vinho} adicionado(s) ao pedido.")
    elif caixaOuGarrafa == 2:
        pedido[vinho] = pedido.get(vinho, 0) + quantidade * 6
        print(f"{quantidade} {vinho} adicionado(s) ao pedido.")

def valorTotalPedido(pedido):
    total = 0
    precos = {'vinho1':90, 'vinho2':110.90, 'vinho3':87.60, 'vinho4': 99.90}
    for item, quantidade in pedido.items():
        if item in precos:
            total =+ quantidade * precos[item]
    return total

def calculafrete():
    frete = valorTotalPedido*0.1 + quantidade * 10
       
        
def main():
    estoque = {'vinho 1: tinto':10, 'vinho 2: rosé':15, 'vinho 3: branco':12, 'vinho 4: frisante':13, 'rolhas': 50, 'rótulos': 70}
    pedido = {}
    precos = {'vinho1':90, 'vinho2':110.90, 'vinho3':87.60, 'vinho4': 99.90}
    caixaOuGarrafa = 0

    while True:
       try:
           print('----------- MENU -----------')
           print('Bem vindo a Vinheria Agnello!')
           mainMenu = int(input('Você é cliente ou funcionário?\n1- Cliente\n2- Funcionário\n3- sair\nEscolha uma opção: ')) 
           match mainMenu:
               case 1:  
                   while True:
                      try:
                          print('----------- MENU -----------')
                          clienteMenu = int(input('Faça seu pedido!\n1- Adicionar vinho ao pedido\n2- Finalizar pedido\n3- Voltar\nEscolha uma opção: ')) 
                          match clienteMenu:  
                              case 1:     
                                     try:
                                         print('Escolha se deseja comprar garrafas ou caixas')
                                         while True:
                                            caixaOuGarrafa = int(input('1- Garrafas\n2- Caixas\nEscolha uma opção: '))
                                            if caixaOuGarrafa == 1 or caixaOuGarrafa == 2:
                                                for vinho, quantidade in estoque.items():
                                                    print(f'{vinho} - quantidade {quantidade}')
                                                vinho = input("Informe o vinho desejado: ")
                                                quantidade = int(input("Informe a quantidade desejada: "))
                                                adicionarPedido(pedido, vinho, quantidade, caixaOuGarrafa)
                                                break
                                            else: 
                                                print('Digite uma opção válida.')
                                     except ValueError:
                                         print('Opção inválida')    
                              case 2: 
                                  subtotalPedido = valorTotalPedido(pedido)
                                  print('Resumo do seu pedido:')
                                  for vinho, quantidade in pedido.items():
                                      print(f'{vinho} - {quantidade}')
                                  print(f'O subtotal do seu pedido é de: {subtotalPedido}')                          

                                  print
                              case 3:
                                  break  
                                     
                              case other: 
                                  print('Digite uma opção válida') 
                      except ValueError:
                          print('Opção inválida')
               case 2:  
                   break
               case 3:  
                   break  
               case other: 
                   print('Digite uma opção válida') 
       except ValueError:
           print('Opção inválida')

main()
