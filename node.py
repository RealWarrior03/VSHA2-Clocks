import queue
import message

# class Node contains Input-Queue, Array to store history of incoming messages
import sequencer


class Node:

    def __init__(self, nodeID, seq):
        self.inbox = queue.Queue()
        self.recieved_messages = []
        self.nodeID = nodeID
        self.seq = seq

    def input_queue(self):
        return self.inbox

    def sendToSeq(self, m):
        self.seq.getSequencerInput().put(m)

    def saveMessage(self, m):
        self.recieved_messages.insert(m.counter, m.payload)

    def thread_runner(self):
        while True:
            if not self.inbox.empty():
                m = self.inbox.get()
                if m.flag == 0:  # External Msg
                    self.sendToSeq(m)
                else:  # Internal Flag
                    self.saveMessage(m)

    def saveToLogFile(self):
        with open("vs_uebung_HA2_gruppe_31/Logs/Node"+ str(self.nodeID)+".txt", 'w') as f:
            #rcvdMsgStr = str(self.recieved_messages)
            for item in self.recieved_messages:
                f.write(str(item))  #TODO does not work
            #f.writelines(rcvdMsgStr)
            f.close()
