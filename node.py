import queue


#class Node contains Input-Queue, Array to store history of incoming messages
class Node:
    inbox = queue.Queue()
    recieved_messages = []

    def input_queue(self):
        return self.inbox

    def poll_messages(self):
        message = self.inbox.get

