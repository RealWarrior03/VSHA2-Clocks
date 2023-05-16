import threading
import queue
import random
import messages

EXTERNAL_FLAG = 0
INTERNAL_FLAG = 1

# assumes nodes and nmbThreads are in scope
def random_messages(nmb_messages):
    for i in range(nmb_messages):
        msg = messages.Message(EXTERNAL_FLAG, random.randrange(0, 1000))
        receiving_thread = random.randrange(0, nmbThreads)
        input_queues[receiving_thread].put(msg)


if __name__ == '__main__':
    nmbThreads = 4

    # Erstelle zwei Threads
    threads = []
    input_queues = []
    # threads and queues are generated and can be access through arrays
    for i in range(nmbThreads):

        myNode = node.Node(i,sequencr)
        nodes.append(myNode)
        sequencr.addNode(myNode)
        threads.append(threading.Thread(target=myNode.thread_runner, args=(i,)))

    for i in range(nmbThreads):  # threads are started
        threads[i].start()

    random_messages(1000, input_queues)

    for i in range(nmbThreads):  # threads are joined in the end to ensure every thread is finished
        threads[i].join()
