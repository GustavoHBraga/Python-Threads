import time
import colorama

from threading import Thread
from queue import Queue


register = [
        {
        'username': 'Gustavo_Braga',
        'nome': 'Gustavo Henrique',
        'idade': '22',
        'cpf': '12312313',
        'email': 'gustavo.braga@threads.com',
        },
        {
        'username': 'Alessly',
        'nome': 'Aless Awesome',
        'idade': '18',
        'cpf': '121313312',
        'email': 'alessly@thread.com'
        },
        {
        'username': 'Mark_Smith',
        'nome': 'Mark Smith',
        'idade': '55',
        'cpf': '121313213',
        'email': 'mark.smith@threads.com'
        },
        {
        'username': 'Claudia_312',
        'nome': 'Claudia Ter',
        'idade': '22',
        'cpf': '213121212',
        'email': 'claudia@threads.com'
        },
        {
        "username": "Paulo_Rodrigues",
        "nome": "Paulo Rodrigues",
        "idade": "40",
        "cpf": "56456456",
        "email": "paulo.rodrigues@example.com"
        },
        {
        "username": "Fernanda_87",
        "nome": "Fernanda Pereira",
        "idade": "25",
        "cpf": "65465465",
        "email": "fernanda.pereira@example.com"
        },
        {
        "username": "Robert_19",
        "nome": "Robert Smith",
        "idade": "33",
        "cpf": "213123123",
        "email": "robert.smith@example.com"
        }
        ]

def gerador_of_thread(register,queue):
    threads = []
    for registro in register:
        threads.append(Thread(target=dados_gerados, args=(queue, registro)))
    
    return threads   

def dados_gerados(queue,register):
    username = register.get('username')
    print(colorama.Fore.BLUE + f'Adicionando um novo registro, Username {username} ', flush=True)
    time.sleep(2)
    queue.put(register)

def consumidor_de_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        name = valor.get('nome')
        print(colorama.Fore.GREEN + f'Dado {name} processado.', flush=True)
        time.sleep(1)
        queue.task_done()

if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado', flush=True)
    
    total_de_registros = len(register)
    print(colorama.Fore.YELLOW + f'Total de registros a serem processados {total_de_registros}', flush=True)
    
    queue = Queue()

    threads = gerador_of_thread(register,queue)
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    threads_queue_consumer = Thread(target=consumidor_de_dados, args=(queue,))
    threads_queue_consumer.start()
    threads_queue_consumer.join()

