import messages
class Sequencer:

  def __init__(self, threadInputQueues):
    self.threadInputQueues = threadInputQueues
    self.sequencerInput = queue.Queue()
    self.counter = 0

  def getSequencerInput(self):
      return self.sequencerInput

  def thread_runner(self):
      while True:
          while not self.sequencerInput.empty():
             exMessage = message.__init__(1,counter)
             self.counter = self.counter+1
             broadcast(self,exMessage)








  def broadcast(self,message):
      for q in self.threadInputQueues:
          q.put(message)