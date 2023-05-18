import sys
import threading
import random
import message
import node

EXTERNAL_FLAG = 0
INTERNAL_FLAG = 1


# assumes nodes and nmbThreads are in scope
def random_messages(nmb_messages):
    for i in range(nmb_messages):
        msg = message.Message(EXTERNAL_FLAG, random.randrange(0, 1000), 0)
        receiving_thread = random.randrange(0, nmbThreads)
        nodes[receiving_thread].input_queue().put(msg)


if __name__ == '__main__':  # param1: nmbThreads, param2: nmbMessages
    nmbThreads = int(sys.argv[1])
    nmbMessages = int(sys.argv[2])

    # Erstelle zwei Threads
    nodeThreads = []
    nodes = []

    # threads and queues are generated and can be access through arrays
    for i in range(nmbThreads):
        myNode = node.Node(i)
        nodes.append(myNode)
        nodeThreads.append(threading.Thread(target=myNode.thread_runner))

    for n in nodes:  # updating notes array of each node, not saving oneself in it
        for diffN in nodes:
            if diffN != n:
                n.nodes.append(diffN)

    for i in range(nmbThreads):  # threads are started
        nodeThreads[i].start()

    random_messages(nmbMessages)

    for i in range(nmbThreads):  # threads are started
        nodes[i].mgSendAllMess = True

    for i in range(nmbThreads):  # threads are joined in the end to ensure every thread is finished
        nodeThreads[i].join()

    for i in range(nmbThreads):  # threads are started
        nodes[i].saveToLogFile()
