#import de bibliotecas necessárias
import json
from datetime import datetime

#Lista principal
tarefas = []

#Função para salvar dados no json
def salvarTarefas():
    with open('tarefas.json', 'w') as arquivo_json:
        json.dump(tarefas, arquivo_json)

#Função para carregar dados do json
def carregarTarefas():
    try:
        with open('tarefas.json', 'r') as arquivo_json:
            tarefas.extend(json.load(arquivo_json))
    except FileNotFoundError:
        tarefas = []

#Função para calcular a completude real
def calcularCompletudeReal(dataFinal):
    formato = "%d/%m/%Y"
    dataFinal = datetime.strptime(dataFinal, formato)
    dataAtual = datetime.now()
    

    diferencaDias = abs((dataAtual - dataFinal).days)
    porcentagem_por_dia = 100 / diferencaDias if diferencaDias != 0 else 0
    
    return porcentagem_por_dia

#Função para calcular a completude planejada
def CalcularCompletudePlanejada(dataInicial, dataFinal):
    formato = "%d/%m/%Y"
    
    data_inicial = datetime.strptime(dataInicial, formato)
    data_final = datetime.strptime(dataFinal, formato)
    
    diferenca_dias = (data_final - data_inicial).days
    
    porcentagem_por_dia = 100 / diferenca_dias if diferenca_dias != 0 else 0
    
    return porcentagem_por_dia

#Função para verificar se a tarefa está em atraso
def verificarAtraso(dataFinal):
    formato = "%d/%m/%Y"
    
    dataFinal = datetime.strptime(dataFinal, formato)
    data_atual = datetime.now()
    
    if data_atual.day > dataFinal.day:
        x = 'Em atraso'
        return x
    else:
        x = 'Em andamento'
        return x

#Adicionar nova tarefa
def addTask():
    nomeTarefa = input('Nome da tarefa: ')
    dataInicial = input('Data inicial (DD/MM/AAAA): ')
    dataFinal = input('Data final (DD/MM/AAAA): ')
    planoAtraso = input('Plano sucinto em caso de atraso: ')
    completudePlanejada = CalcularCompletudePlanejada(dataInicial, dataFinal)
    CompletudeReal = calcularCompletudeReal(dataFinal)
    status = verificarAtraso(dataFinal)

    tarefa = {
        'nomeTarefa': nomeTarefa,
        'dataInicial': dataInicial,
        'dataFinal': dataFinal,
        'completudePlanejada': completudePlanejada,
        'CompletudeReal': CompletudeReal,
        'planoAtraso': planoAtraso,
        'status': status
        }
    
    tarefas.append(tarefa)
    salvarTarefas()
    
#Função para remover a tarefa   
def remTask():
    print('Tarefas:')
    for i, tarefa in enumerate(tarefas):
        print(f'{i + 1}. {tarefa["nomeTarefa"]}')
    try:
        indice = int(input('Digite o número da tarefa que deseja remover: ')) - 1
        if 0 <= indice < len(tarefas):
            del tarefas[indice]
            print('Tarefa removida com sucesso!')
            salvarTarefas()
        else:
            print('Índice inválido.')
    except ValueError:
        print('Valor inválido. Certifique-se de inserir um número.')
        
#Função para atualizar tarefas
def updateTask():
    print('Atualizar uma tarefa específica:')
    for i, task in enumerate(tarefas):
        print(f'{i + 1}. {task["nomeTarefa"]}')
    try:
        num_tarefa = int(input('Digite o número da tarefa que deseja atualizar: ')) - 1
        if 0 <= num_tarefa < len(tarefas):
            task = tarefas[num_tarefa]
            print(f'Tarefa: {task["nomeTarefa"]}')
            print(f'Data Inicial: {task["dataInicial"]}')
            print(f'Data Final: {task["dataFinal"]}')
            print(f'Completude Planejada: {task["completudePlanejada"]}%')
            print(f'Completude Real: {task["CompletudeReal"]}%')
            print(f'Status: {task["status"]}')
            novo_nome = input('Novo nome (deixe em branco para manter o mesmo): ')
            nova_data_inicial = input('Nova data inicial (DD/MM/AAAA) (deixe em branco para manter a mesma): ')
            nova_data_final = input('Nova data final (DD/MM/AAAA) (deixe em branco para manter a mesma): ')
            novo_completude_real = calcularCompletudeReal(nova_data_final) if nova_data_final else task['CompletudeReal']
            task['nomeTarefa'] = novo_nome if novo_nome else task['nomeTarefa']
            task['dataInicial'] = nova_data_inicial if nova_data_inicial else task['dataInicial']
            task['dataFinal'] = nova_data_final if nova_data_final else task['dataFinal']
            task['CompletudeReal'] = novo_completude_real

            if nova_data_inicial and nova_data_final:
                task['completudePlanejada'] = CalcularCompletudePlanejada(nova_data_inicial, nova_data_final)
                task['status'] = verificarAtraso(nova_data_final)
            print('Tarefa atualizada com sucesso!')
            salvarTarefas()
        else:
            print('Índice inválido.')
    except ValueError:
        print('Valor inválido. Certifique-se de inserir um número válido.')

#Função para visualização das tarefas em lista
def visuTask():
    print('Visualizar uma tarefa específica:')
    for i, task in enumerate(tarefas):
        print(f'{i + 1}. {task["nomeTarefa"]}')
    try:
        num_tarefa = int(input('Digite o número da tarefa que deseja visualizar: ')) - 1
        if 0 <= num_tarefa < len(tarefas):
            task = tarefas[num_tarefa]
            print(f'Tarefa: {task["nomeTarefa"]}')
            print(f'Data Inicial: {task["dataInicial"]}')
            print(f'Data Final: {task["dataFinal"]}')
            print(f'Completude Planejada: {task["completudePlanejada"]}%')
            print(f'Completude Real: {task["CompletudeReal"]}%')
            print(f'Status: {task["status"]}')
            print(f'Plano de Atraso: {task["planoAtraso"]}')
        else:
            print('Índice inválido.')
    except ValueError:
        print('Valor inválido. Certifique-se de inserir um número válido.')

#Função para o menu
def main():
    carregarTarefas()
    while True:
        try:
            print('-' * 40)
            menu = int(input('Tarefas de modernização da Vinheria Agnello \n Escolha uma opção: \n 1 - Adicionar Tarefa \n 2 - Remover tarefa \n 3 - Atualizar tarefa \n 4 - Visualizar tarefa \n 5 - sair \n'))
            match menu:
                case 1: 
                    addTask()
                case 2: 
                    remTask()
                case 3: 
                    updateTask()
                case 4:
                    visuTask()
                case 5:
                    break
                case other: 
                    print('Opção inválida')  
        except ValueError:
            print('Opção inválida')  
            
main()