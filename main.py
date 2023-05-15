import threading
import queue

def thread_runner(id):
    print(id)

if __name__ == '__main__':
    nmbThreads = 4

    # Erstelle zwei Threads
    threads = []
    input_queues = []
    for i in range(nmbThreads):
        threads.append(threading.Thread(target=thread_runner(i)))
        input_queues.append(queue.Queue())

    for i in range(nmbThreads):
        threads[i].start()

    for i in range(nmbThreads):
        threads[i].join()
