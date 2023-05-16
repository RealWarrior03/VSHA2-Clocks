import queue
import messages


#class Node contains Input-Queue, Array to store history of incoming messages
import sequencer
class Node:


    def __init__(self,nodeID,seq):
        inbox = queue.Queue()
        self.recieved_messages = []
        self.nodeID=nodeID
        self.seq = seq


    def input_queue(self):
        return self.inbox

    def thread_runner(self):
        while True:
            if not self.inbox.empty():
                message = self.inbox.get
                if message.flag == EXTERNAL_FLAG: #External Msg
                    sendToSeq(message)
                else:                 #Internal Flag
                    saveMessage(message)






    def sendToSeq(self,message):
        self.seq.getSequencerInput.put(message)

    def saveMessage(self,message):
        self.recieved_messages[message.counter] = message.payload

    def saveToLogFile(self):
         with open(self.id, 'w') as f:
             for item in self.recieved_messages:
                 f.write(f'{item}\n')
