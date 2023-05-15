import threading
import queue

def thread_runner(id):
    while True:
        while not input_queues[id].empty():
            data = input_queues[id].get()
            print(f"Processing data: {data}")
            print(f"thread id: {id} ")

if __name__ == '__main__':
    nmbThreads = 4

    # Erstelle zwei Threads
    threads = []
    input_queues = []
    for i in range(nmbThreads):
        input_queues.append(queue.Queue())
        threads.append(threading.Thread(target=thread_runner, args=(i,)))

    for i in range(nmbThreads):
        threads[i].start()

    input_queues[0].put("hey first thread")
    input_queues[2].put("hello second thread")

    for i in range(nmbThreads):
        threads[i].join()
