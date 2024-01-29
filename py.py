dados = [
    {'id': 1, 'desc': 'Estudar react', 'prioridade': 3, 'categoria': 'estudo', 'status': 'pendente'},
    {'id': 2, 'desc': 'Estudar js', 'prioridade': 1, 'categoria': 'estudo', 'status': 'concluido'}
]

for tarefa in dados:
    print(tarefa)


def listar_tarefas():
    print(dados)


def add_taferas():

    novo_id = int(input('Digite o id da nova tarefa: ')) 
    nova_descricao = input('Digite a descrição da nova tarefa: ')
    nova_prioridade = int(input('Digite a prioridade da nova tarefa: '))
    nova_categoria = input('Digite a categoria da nova tarefa: ')
    novo_status = input('Digite o status da nova tarefa: ')

    nova_tarefa = {'id': novo_id, 'desc': nova_descricao, 'prioridade': nova_prioridade, 'categoria': nova_categoria, 'status': novo_status}

    dados.append(nova_tarefa)
    print('Tarefa adicionada com sucesso!')


def remover_taferas():
    rem = int(input('Digite qual ID da tarefa que deseja remover: '))
    
    apagar = {}

    for item in dados:
        if item['id'] == rem:
            apagar = item
            break

    dados.remove(apagar)


def conc_taferas():
    conc = int(input('Digite o ID da tarefa que deseja concluir: '))

    for item in dados:
        if item['id'] == conc:
            apagar = item
            break

    dados.remove(apagar)

while True:
    print(f'''
        ======================TAREFAS======================
        ||                                               || 
        ||                    OPÇÕES :                   ||
        ||                                               ||
        ||           1 - Incluir uma nova tarefa.        ||
        ||           2 - Excluir uma tarefa.             ||
        ||           3 - Concluir uma tarefa.            ||
        ||           4 - Listar tarefas.                 ||
        ||           X - Encerrar aplicação.             ||
        ||                                               ||
        ===================================================     
    ''')

    op = input('Informe a opção desejada: ')

    if op == 'X':
        print('...Encerrando aplicação! ')
        break
    elif op == '4':
        print('...Listando tarefas! ')
        listar_tarefas()
    elif op == '1':
        print('...Insira sua nova tarefa: ')
        add_taferas()
    elif op == '2':
        print('...Excluir tarefa!')
        remover_taferas()
    elif op == '3':
        print('...Concluindo tarefa! ')
        conc_taferas()