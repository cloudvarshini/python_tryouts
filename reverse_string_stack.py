class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None

    def push(self, s):
        new_node = Node(s)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        tem_head = self.head
        while tem_head is not None:
            print(tem_head.data, end="")
            tem_head = tem_head.next
        print()


if __name__ == "__main__":
    S = stack()
    str = input()
    for i in str:
        S.push(i)
    S.reverse()