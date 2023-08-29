"""
Gabriel Machado Belardino
Kaiky Alvaro de Miranda
Lucas Rodrigues da Silva
Pedro Henrique Bicas Couto
Ana Beatriz Farah Alves
"""

import sys                                                                                                                                                                                                                   

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
        
def adicionarPedido(pedido, estoque, vinho, quantidade, caixaOuGarrafa):
    if caixaOuGarrafa == 1:
        if vinho in estoque and estoque[item] >= quantidade:
            pedido[vinho] = pedido.get(vinho, 0) + quantidade
            print(f"{quantidade} {vinho} adicionado(s) ao pedido.")
        else:
            print("Item não identificado.")
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
                                  break  
                              case 3:
                                  break 
                              case other: 
                                  print('Digite uma opção válida') 
                      except ValueError:
                          print('Opção inválida')
               case 2:  
                   while True:
                      try:
                          print('----------- MENU -----------')
                          clienteMenu = int(input('1- Registrar entrada\n2 - Registrar saída\n3- Voltar\nEscolha uma opção: ')) 
                          match clienteMenu:  
                              case 1:     
                                     try:
                                         vinho = input("Informe o item que deseja registrar a entrada: ")
                                         quantidade = int(input("Informe a quantidade: "))
                                         registrarEntrada(estoque, vinho, quantidade)
                                     except ValueError:
                                         print('Opção inválida')    
                              case 2: 
                                    try:
                                         vinho = input("Informe o item que deseja registrar a saída: ")
                                         quantidade = int(input("Informe a quantidade: "))
                                         registrarSaida(estoque, vinho, quantidade)
                                    except ValueError:
                                         print('Opção inválida')   
                              case 3:
                                  break 
                              case other: 
                                  print('Digite uma opção válida') 
                      except ValueError:
                          print('Opção inválida')
                   break
               case 3:  
                   break  
               case other: 
                   print('Digite uma opção válida') 
       except ValueError:
           print('Opção inválida')

main()
