"""
Новая неисследованная вершина nbr окрашивается в серый.

Предшественником nbr устанавливается текущий узел currentVert.

Расстояние nbr устанавливается равным расстоянию currentVert + 1.

nbr добавляется в конец очереди. Это эффективно планирует дальнейшее исследование узла,
но не прежде, чем будут исследованы прочие вершины из списка смежности currentVert.
"""

from Graphs.Implementation import Graph, Vertex
from LinearStructures.Queue.Queue import Queue

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while(vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()

        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while(x.getPred()):
        print(x.getId())
        x = x.getPred
    print(x.getId())

