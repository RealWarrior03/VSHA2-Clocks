import messages
import queue
class Sequencer:

  def __init__(self):
    self.sequencerInput = queue.Queue()
    self.counter = 0
    self.nodes = []

  def getSequencerInput(self):
      return self.sequencerInput

  def thread_runner(self):
      while True:
          if not self.sequencerInput.empty():
             msgToBroadcast = self.sequencerInput.get()
             exMessage = message.Message(1,msgToBroadcast.payload,counter)
             self.counter = self.counter+1
             broadcast(self,exMessage)

  def addNode(self,node):
      self.nodes.append(node)








  def broadcast(self,message):
      for n in self.nodes:
          n.input_queue().put(message)