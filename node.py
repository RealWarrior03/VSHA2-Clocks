import queue
import messages


#class Node contains Input-Queue, Array to store history of incoming messages
class Node:
    inbox = queue.Queue()
    recieved_messages = []

    def input_queue(self):
        return self.inbox

    def poll_messages(self):
        if not self.inbox.empty():
            message = self.inbox.get
        #if message.flag == 0:


