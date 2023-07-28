
from threading import Thread 
import time

def main():
    # Multi Treads
    th = [
        Thread(target=contar, args=('elefante',10)),
        Thread(target=contar, args=('Macaco',10)),
        Thread(target=contar, args=('Rato',5)),
        Thread(target=contar, args=('Coelho',22))
        ]
    
    [th.start() for th in th]

    # Executo outras coisas enquanto a thread está executando...
    print('Podemos fazer outras coisas no programa enquanto a thread esta executando...')
    
    # Aguardo 3 segundos para continuar... o programa em paralelo com a thread
    time.sleep(3)
    print('Aguardando a Thread terminar...')

    [th.join() for th in th]

    print('Pronto! Thread terminou.')

def contar(o_que, numero):
    for i in range(1, numero + 1):
        print(f'{i} {o_que}(s)...')
        time.sleep(1)

if __name__ == '__main__':
    main()