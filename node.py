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
            print("path not found, but now created :)")

        filename = "Node" + str(self.nodeID) + ".txt"
        fullpath = os.path.join(path, filename)
        print(fullpath)
        with open(fullpath, 'w') as file:
        #with open("vs_uebung_HA2_gruppe_31/Logs/Node"+ str(self.nodeID)+".txt", 'w') as f:
            #rcvdMsgStr = str(self.received_messages)
            print("messages: " + str(self.received_messages))
            print("inbox: " + str(list(self.inbox.queue)))
            for item in self.received_messages:
                print(str(item))
                file.write(str(item))  #TODO does not work
                print("received message written to the logs")
            #f.writelines(rcvdMsgStr)
            file.close()
            print("file successfully closed")
