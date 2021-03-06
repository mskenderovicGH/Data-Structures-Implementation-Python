# Class Stack will implement stack abstract data structure (Last in - First out)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack==[]

    def stack_size(self):
        return len(self.stack)
