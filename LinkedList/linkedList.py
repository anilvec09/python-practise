
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0


    def insertAtBegin(self,data):
         self.numOfNodes = self.numOfNodes + 1
         new_node = Node(data)

         if self.head is None:
             self.head = new_node
         else:
             new_node.nextNode = self.head
             self.head = new_node



    def insertAtEnd(self,data):

        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node



    def traverse(self):

        actual_node = self.head

        if actual_node is not None:
            while actual_node is not None:
                 print(actual_node.data)
                 actual_node = actual_node.nextNode
        else: print("Empty")


    def remove(self,inp_data):

        if self.head is None:
            return "Empty"

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != inp_data:
            previous_node = actual_node
            actual_node =  actual_node.nextNode

        if actual_node is None:
            return "not present"

        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode


linklist1 = LinkedList()
linklist1.insertAtBegin(10)
linklist1.insertAtBegin(20)
linklist1.insertAtBegin(30)
linklist1.insertAtBegin(40)
linklist1.insertAtEnd(50)
# linklist1.remove(6000)
linklist1.remove(10)
linklist1.traverse()