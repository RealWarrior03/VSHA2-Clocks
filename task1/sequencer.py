import message
import queue


class Sequencer:

    def __init__(self):
        self.sequencerInput = queue.Queue()
        self.counter = 0
        self.nodes = []
        self.sendAllMess = False

    def getSequencerInput(self):
        return self.sequencerInput

    def thread_runner(self):
        while not self.allNodesFinished() or not self.sequencerInput.empty():   #waits until nodes send all of their messages to the seq and queue empty
            if not self.sequencerInput.empty():
                msgToBroadcast = self.sequencerInput.get()
                exMessage = message.Message(1, msgToBroadcast.payload, self.counter)
                self.counter = self.counter + 1
                self.broadcast(exMessage)

        self.sendAllMess = True

    def addNode(self, node):
        self.nodes.append(node)

    def broadcast(self, m):
        for n in self.nodes:
            n.input_queue().put(m)

    def allNodesFinished(self):
        if len(self.nodes) == 0:
            allFinished = False
        else:
            allFinished = True

        for n in self.nodes:
            if not n.sendAllMess:
                allFinished = False
        return allFinished
