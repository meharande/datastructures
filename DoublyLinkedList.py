
class Node:
    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        return self.head

    def insertAfter(self, newData, prevNode):
        if prevNode is None:
            print('Given not is not presented in DLL')
            return
        newNode = Node(data = newData)
        newNode.next = prevNode.next
        if prevNode.next is not None:
            prevNode.next.prev = newNode
        prevNode.next = newNode
        newNode.prev = prevNode
        return newNode

    def append(self, newData):
        newNode = Node(data = newData)
        newNode.next = None

        lastNode = self.head
        if self.head is None:
            self.head = newNode
            self.head.prev = None
            return

        while lastNode.next is not None:
            lastNode = lastNode.next

        lastNode.next = newNode
        newNode.prev = lastNode
        return newNode

    def insertBefore(self, newData, nextNode):
        if nextNode is None:
            print('Reference node is not presented in DLL')
            return

        newNode = Node(data = newData)
        newNode.prev = nextNode.prev
        if nextNode.prev is not None:
            nextNode.prev.next = newNode
        else:
            self.head = newNode

        newNode.next = nextNode
        nextNode.prev = newNode
        return newNode

    def traverse(self, node):
        last = None
        print("Traversal in forward direction \n")
        while node is not None:
            print(node.data, end=" ")
            last = node
            node = node.next
        print("\nTraversal in backward direction \n")
        while last is not None:
            print(last.data, end=" ")
            last = last.prev


doublyLinkedList = DoublyLinkedList()
headNode = doublyLinkedList.push('Monday')
nodeA = doublyLinkedList.append('Tuesday')
nodeB = doublyLinkedList.append('Thursday')
nodeC = doublyLinkedList.insertBefore('Wednesday', nodeA.next)
nodeD = doublyLinkedList.insertAfter('Friday', nodeB)
doublyLinkedList.traverse(headNode)