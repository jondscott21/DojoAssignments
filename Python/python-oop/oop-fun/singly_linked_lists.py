class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def PrintAllVals(self):
        runner = list.head
        while runner is not None
            print(runner.val)
            runner = runner.next
    def AddBack(self, val):
        runner = list.head
        while runner is not None:
            runner = runner.next
            if runner.next is None
                print "bobbbbb"
                runner.next = Node(val)


    # def AddFront(self):
    # def InsertBefore(self):
    # def InsertAfter(self):
    # def RemoveNode(self):
    # def ReverseList(self):
list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
list.tail = Node('Debra')
list.AddBack('Bob')

# list.PrintAllVals()