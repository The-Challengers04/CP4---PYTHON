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
        
        
        
def main():
    estoque = {'vinho1':10, 'vinho2':15, 'vinho3':12, 'vinho4':13}
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
                          clienteMenu = int(input('Faça seu pedido!\n1- Adicionar vinho ao pedido\n2- Finalizar pedido\n3- sair\nEscolha uma opção: ')) 
                          match clienteMenu:  
                              case 1: 
                                     
                                     try:
                                         print('Escolha se deseja comprar garrafas ou caixas')
                                         caixaOuGarrafa = int(input('1- Garrafas\n2- Caixas\nEscolha uma opção: '))
                                         #if caixaOuGarrafa == 1 or caixaOuGarrafa == n2:
                                     except ValueError:
                                         print('Opção inválida')
                                     vinho = input("Informe o vinho desejado: ")
                                     quantidade = int(input("Informe a quantidade desejada: "))
                                     adicionarPedido(estoque, vinho, quantidade, caixaOuGarrafa)
                              case 2: 
                                  break 
                              case 3:
                                  break  
                                     
                              case other: 
                                  print('Digite uma opção válida') 
                      except ValueError:
                          print('Opção inválida')
               case 2:  
                   break
               case 4:  
                   break  
               case other: 
                   print('Digite uma opção válida') 
       except ValueError:
           print('Opção inválida')




main()