import threading
import queue

EXTERNAL_FLAG = 0
INTERNAL_FLAG = 1


def thread_runner(id):
    while True:
        while not input_queues[id].empty():  # checks for new messages in input_queue
            data = input_queues[id].get()  # get data out of input_queue

            # process data
            payload = data.payload
            print(f"Processing data: {payload}")
            print(f"thread id: {id} ")


def message_sequencer_runner(nmbThreads):
    print("Test")


if __name__ == '__main__':
    nmbThreads = 4

    # Erstelle zwei Threads
    threads = []
    input_queues = []
    # threads and queues are generated and can be access through arrays
    for i in range(nmbThreads):
        input_queues.append(queue.Queue())
        threads.append(threading.Thread(target=thread_runner, args=(i,)))

    for i in range(nmbThreads):  # threads are started
        threads[i].start()

    # data transfer test
    m = Message(EXTERNAL_FLAG, "hey first thread")
    input_queues[0].put(m)


    for i in range(nmbThreads):  # threads are joined in the end to ensure every thread is finished
        threads[i].join()
