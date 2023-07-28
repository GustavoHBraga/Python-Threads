
from threading import Thread 
import time

list_o_que = []

def createListThreads(target, args):
    threads = []
    for arg in args:
        t = Thread(target=target, args=(arg[0],arg[1]))
        threads.append(t)
    return threads

def listInfoCentral(info,list):
    list.append(info)
    return list

def contar(o_que, numero):
    global list_o_que
    listInfoCentral([o_que,numero],list_o_que)
    for i in range(1, numero + 1):
        print(f'{i} {o_que}(s)...')
        time.sleep(1)


def main():
    args = [
        ['elefante',10],
        ['Macaco',10],
        ['Rato',10],
        ['Coelho',10],
        ['leao',10],
        ['Cao',10],
        ['Passaro',10],
        ['cobra',10],
        ['Aranha',10]
    ]
    
    th = createListThreads(contar, args)
    
    print(f'TOTAL DE THREADS: {len(th)}')
    
    [th.start() for th in th]
    [th.join() for th in th]
    print('Pronto! Thread terminou.')
    print(list_o_que)

if __name__ == '__main__':
    main()