from module1 import main1

import winsound, sys
from threading import Thread
from time import sleep
from queue import Queue


q = Queue()

def threaded_function(arg):
    
    
    winsound.PlaySound(file, winsound.SND_FILENAME)
    winsound.PlaySound(file, winsound.SND_FILENAME)

    

def worker():
    
    while True:
        #if q.empty():
        #    sleep(50)
        #    continue
        item = q.get()
        if item == 'exit':
            break
        else:
            file = '../wav/moan_1.wav'  
            winsound.PlaySound(file, winsound.SND_FILENAME)


if __name__ == "__main__":
    main1()


    #t = Thread(target=worker)
    #t.daemon = False
    #t.start()

    #for item in source():
    #q.put('str1')
    #q.put('str2')
    #q.put('exit')

    #q.join()       # block until all tasks are done
    #print ("thread finished...exiting")
