import threading
import queue
import random
import message
import node
import sequencer

EXTERNAL_FLAG = 0
INTERNAL_FLAG = 1


# assumes nodes and nmbThreads are in scope
def random_messages(nmb_messages):
    for i in range(nmb_messages):
        msg = message.Message(EXTERNAL_FLAG, random.randrange(0, 1000))
        receiving_thread = random.randrange(0, nmbThreads)
        nodes[receiving_thread].input_queue().put(msg)

if __name__ == '__main__':
    nmbThreads = 1

    # Erstelle zwei Threads
    nodeThreads = []
    nodes = []

    sequencr = sequencer.Sequencer()
    seqThread = threading.Thread(target=sequencr.thread_runner)
    seqThread.start()

    # threads and queues are generated and can be access through arrays
    for i in range(nmbThreads):
        myNode = node.Node(i, sequencr)
        nodes.append(myNode)
        sequencr.addNode(myNode)
        nodeThreads.append(threading.Thread(target=myNode.thread_runner))

    for i in range(nmbThreads):  # threads are started
        nodeThreads[i].start()

    random_messages(1)

    for i in range(nmbThreads):  # threads are joined in the end to ensure every thread is finished
        nodes[i].saveToLogFile()
        nodeThreads[i].join()
        seqThread.join()
