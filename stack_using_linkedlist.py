class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    def push(self,num):
        new_node = Node(num)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        tem_head = self.head
        if (tem_head is None):
            print("Empty stack")  
        else:    
            print("Current stack")
            while tem_head is not None:
                print(tem_head.data)
                tem_head = tem_head.next  
    def pop(self):
        if (self.head is None):
            print("List has no element")
        else:
            self.head = self.head.next    

if __name__ == "__main__":
    S = stack()
    i = int(input())
    while (i>=0):
        S.push(i)
        i = int(input())
    S.print()
    S.pop()
    S.print()

    

