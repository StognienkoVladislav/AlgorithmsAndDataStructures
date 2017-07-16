from LinearStructures.Queue.Queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    print(" ".join(namelist) + " Start game")
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        print(simqueue.dequeue() +' leave')

    return simqueue.dequeue()

if __name__ == '__main__':
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7) + " WIN")