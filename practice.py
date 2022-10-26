class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = self
    def push(self,s):
        new_node = Node(s)
        new_node.next = self.head
        self.head = new_node
        
    def reverse(self):
        tem_head = self.head
        while tem_head is not None:
            return tem_head.data
            tem_head = tem_head.next
        print()
        
if __name__ == "__main__":
    S = stack()
    st= input()
    for i in st:
        S.push(i)
    l = []
    for i in S.reverse() :
        l1 = l.append(i)
    print(l)
    if (st==l):
        print("Palindrome")
    else:
        print("Not Palindrome")