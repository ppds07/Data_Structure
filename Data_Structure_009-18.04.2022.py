class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.next = None
 
 
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0
 
    def dequeue(self):          # delete at the beginning
        if self.front is None:
            print('Queue Underflow')
            exit(-1)
 
        temp = self.front
        print('Removing…', temp.data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None
 
        self.count -= 1
 
        return temp.data
 
 
    def enqueue(self, item):    # insertion at the end
        node = Node(item)
        print('Inserting…', item)
 
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
 
        self.count += 1
 
    def peek(self):

        if self.front:
            return self.front.data
        else:
            exit(-1)
 
    def isEmpty(self):
        return self.rear is None and self.front is None

    def size(self):
        return self.count
 
 
if __name__ == '__main__':
 
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print('The front element is', q.peek())
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    if q.isEmpty():
        print('The queue is empty')
    else:
        print('The queue is not empty')
