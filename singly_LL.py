class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def iatstart(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode
    def iatend(self,newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newnode
    def iatpos(self,prevnode,newdata):
        if prevnode is None:
            print("Node must be in this linked list")
            return
        newnode = Node(newdata)
        newnode.next = prevnode.next
        prevnode.next = newnode
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
if __name__ == "__main__":
    llist = linkedlist()
    llist.iatend(6)
    llist.iatstart(10)
    llist.iatend(11)
    llist.iatpos(llist.head.next,8)
    print("Created linked list:")
    llist.printlist()
