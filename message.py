class Message:
    def __init__(self, flag, payload, counter=-1):
        self.flag = flag
        self.payload = payload
        self.counter = counter
