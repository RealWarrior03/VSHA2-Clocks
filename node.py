import queue
import message


#class Node contains Input-Queue, Array to store history of incoming messages
import sequencer
class Node:

    def __init__(self,nodeID,seq):
        self.inbox = queue.Queue()
        self.recieved_messages = []
        self.nodeID=nodeID
        self.seq = seq


    def input_queue(self):
        return self.inbox


    def thread_runner(self):
        while True:
            if not self.inbox.empty():
                message = self.inbox.get()
                if message.flag == 0: #External Msg
                    self.sendToSeq(message)
                else:                 #Internal Flag
                    self.saveMessage(message)

    def saveToLogFile(self):
         with open("Logs/Node_"+str(self.nodeID)+".txt", 'w') as f:
             for item in self.recieved_messages:
                 f.write(f'{item}\n')
             f.close

