class queue():
    def __init__(self, startingValue=None):
        self.values = []
        if startingValue is not None:
            self.values.append(startingValue)

    def add(self, value):
        self.values.append(value)

    def pull(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        out = self.values[0]
        self.values = self.values[1:]
        return out

    def peek(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        return self.values[0]

    def isEmpty(self):
        if len(self.values) == 0:
            return True
        else:
            return False
