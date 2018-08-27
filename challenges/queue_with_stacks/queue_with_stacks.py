class Queue(object):
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def enqueue(self, val):
        for i in self.stack_two:
            self.stack_one.push(self.stack_two.pop())
        return self.stack_one.push(val)

    def dequeue(self):
        for i in self.stack_one:
            self.stack_two.push(self.stack_one.pop())
        return self.stack_two.pop()
