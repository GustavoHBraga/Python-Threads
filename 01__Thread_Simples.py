
from threading import Thread 
import time

def main():
    th = Thread(target=contar, args=('elefante',10))
    th.start() # Deixo a thread pronta para entrar na fila de execucao do sistema operacional

    # Executo outras coisas enquanto a thread está executando...
    print('Podemos fazer outras coisas no programa enquanto a thread esta executando...')
    print('Gustavo')
    print('Gustavo Henrique')
    print('Gustavo Braga')

    # Aguardo 3 segundos para continuar... o programa em paralelo com a thread
    time.sleep(3)
    print('Aguardando a Thread terminar...')

    th.join() # Apartir desse momento aguardo a Thread terminar para continuar o programa
    print('Pronto! Thread terminou.')

def contar(o_que, numero):
    for i in range(1, numero + 1):
        print(f'{i} {o_que}(s)...\n')
        time.sleep(1)

if __name__ == '__main__':
    main()