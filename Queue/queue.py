from collections import deque

class Queue:

    def __init__(self):
        self.container = deque()


    def push(self, value):
        self.container.insert(0, value)


    def pop(self):
        return self.container.pop()
    

    def peek(self):
        return self.container[-1]
    

    def isEmpty(self):
        return len(self.container)==0
    

    def size(self):
        return len(self.container)
    
    
if __name__ == '__main__':
    queue = Queue()
    queue.push(5)
    queue.push(7)
    print(queue.peek())
    print(queue.pop())