class Stack(object):

    @staticmethod
    def about():
        print('I am a stack object, so I am really important:)')

    def __init__(self):
        self.stack = []

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)


# Stack class is almost identical to the list class, so just inherit it...
class StackD(list):
    def push(self, obj):
        self.append(obj)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)

    while stack.length() > 0:
        print(stack.pop())

    stack2 = StackD()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    print(stack2)

    while len(stack2):
        print(stack2.pop())

    # static method
    stack.about()
