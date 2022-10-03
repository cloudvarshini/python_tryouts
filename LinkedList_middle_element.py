class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next 
    def print_middle_node(self):
        tem_head = self.head
        count = 0
        while tem_head is not None:
            count = count+1
            tem_head = tem_head.next
        #print(count)
        if (count==0):
            print("Emty linkedlist.")
        else:    
            middle = round(count/2)
            print(middle)
            tem_head = self.head
            for i in range(1,middle):  
                tem_head = tem_head.next
            print(tem_head.data)             
            
list = SLL()
#list.head = Node("Mon")
#e2 = Node("Tue")
#e3 = Node("Wen")
#e4 = Node("Thu")
#list.head.next = e2
#e2.next = e3
#e3.next = e4
list.listprint()
list.print_middle_node()