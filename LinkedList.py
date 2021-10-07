
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def inset_atEnd(self, NewData):
        newNode = Node(NewData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = newNode
        return newNode

    def insert_inMiddle(self, middleNode, newData):
        if middleNode is None:
            print("Please add middle node")
            return
        newNode = Node(newData)
        newNode.next = middleNode.next
        middleNode.next = newNode

    def removeNode(self, trashData):
        headVAl = self.head

        if(headVAl is not None):
            if(headVAl.data == trashData)


    def traverse(self):
        if self.head is None:
            return

        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next




linkedlist = LinkedList()
linkedlist.head = Node("Monday")
second = Node("Tuesday")
third = Node("Wednesday")

linkedlist.head.next = second
second.next = third

fourth =linkedlist.inset_atEnd('Thursday')
fifth =linkedlist.inset_atEnd('Friday')
sixth = linkedlist.inset_atEnd('Sunday')
linkedlist.insert_inMiddle(fifth, 'Saturday')
linkedlist.traverse()
