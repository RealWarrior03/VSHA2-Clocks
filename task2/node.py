import queue
import message
import os

# class Node contains Input-Queue, Array to store history of incoming messages


class Node:

    def __init__(self, nodeID):
        self.inbox = queue.Queue()
        self.received_messages = []
        self.counter = 0

        self.nodeID = nodeID
        self.nodes = []

        self.mgSendAllMess = False
        self.sendAllMess = False

    def input_queue(self):
        return self.inbox

    def saveMessage(self, m):
        if m.counter <= self.counter and m.nodeId < self.nodeID:
            self.received_messages.insert(m.counter, m.payload)
        else:
            self.received_messages.append(m.payload)

    def thread_runner(self):
        while not self.allNodesFinished() or not self.inbox.empty() or self.mgSendAllMess:   #waits until seq send all of its messages to the nodes and queue empty
            if not self.inbox.empty():
                m = self.inbox.get()
                if m.flag == 0:  # External Msg
                    m = message.Message(1, m.payload, self.nodeID, self.counter)
                    self.counter = self.counter + 1
                    self.saveMessage(m)
                    self.broadcast(m)
                else:  # Internal Flag
                    self.saveMessage(m)
            """if self.inbox.empty() and self.mgSendAllMess:
                self.sendAllMess = True"""

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

    def allNodesFinished(self):
        if len(self.nodes) == 0:
            allFinished = False
        else:
            allFinished = True

        for n in self.nodes:
            if not n.sendAllMess:
                allFinished = False
        return allFinished

    def broadcast(self, m):
        for n in self.nodes:
            n.input_queue().put(m)
