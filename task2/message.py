class Message:
    def __init__(self, flag, payload, nodeId, counter=-1):
        self.flag = flag
        self.payload = payload
        self.nodeId = nodeId
        self.counter = counter

