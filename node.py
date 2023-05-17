import queue
import message
import os

# class Node contains Input-Queue, Array to store history of incoming messages
import sequencer


class Node:

    def __init__(self, nodeID, seq):
        self.inbox = queue.Queue()
        self.received_messages = []
        self.nodeID = nodeID
        self.seq = seq

    def input_queue(self):
        return self.inbox

    def sendToSeq(self, m):
        self.seq.getSequencerInput().put(m)

    def saveMessage(self, m):
        self.received_messages.insert(m.counter, m.payload)

    def thread_runner(self):
        while True:
            if not self.inbox.empty():
                m = self.inbox.get()
                if m.flag == 0:  # External Msg
                    self.sendToSeq(m)
                else:  # Internal Flag
                    self.saveMessage(m)

    def saveToLogFile(self):
        path = os.getcwd() + "/Logs/"
        if not os.path.exists(path):
            os.makedirs(path)

        filename = "Node" + str(self.nodeID) + ".txt"
        fullpath = os.path.join(path, filename)
        with open(fullpath, 'w') as file:
            for item in self.received_messages:
                file.write(str(item) + "\n")  #TODO does not work
            #f.writelines(rcvdMsgStr)
            file.close()
