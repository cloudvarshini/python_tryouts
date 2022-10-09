class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def insert(self,num):
        new_node = Node(num)
        if (self.front == None and self.rear == None):
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def print(self):
        tem_front = self.front
        if (self.front is None):
            print("Empty Queue.")
        else:    
            print("Current Queue.")
            while tem_front is not None:
                print(tem_front.data)
                tem_front = tem_front.next
    def delete(self):
        if (self.front is None):
            print("Queue has no elements.")
        else:    
            self.front = self.front.next

Q = Queue()
i = int(input())
while (i>=0):
    Q.insert(i)
    i = int(input())
Q.print()
Q.delete()
Q.print()
