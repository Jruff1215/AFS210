
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.length = 0
        
    def push(self, data):
        node = Node(data)
        if self.length == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.length += 1
        
    def pop(self):
        self.top = self.top.next
        return self.top.data
    
    def size(self):
        return self.length
    
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    
    def peek(self):
        return self.top

class Queue:
    def __init__(self) -> None:
        self.list = []
        
    def enqueue(self, data):
        self.list.append(data)
        
    def dequeue(self):
        self.list.pop()
        
    def size(self):
        return len(self.list)
        
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
        
    def peek(self):
        last = self.list[-1]
        return last

class Node:
     def __init__(self, data=None):
        self.data = data
        self.next = None

def isPalindrome(data):
    queue = Queue()
    stack = Stack()
    queue.enqueue(data)
    first = list(queue.list[0])
    first.reverse()
    stack.push(first)
    if list(queue.list[0]) == stack.top.data:
        return True
    else:
        return False
    
print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))
