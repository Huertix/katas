class Node():
    next = None
    previous = None
    data = None

    def __init__(self, data):
        self.data = data


class LinkedList():
    head = None

    # O(n)
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)

    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead  # change the new head pointer

    # O(n)
    def deleteWithValue(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

    def printList(self):

        if not self.head:
            return
        current = self.head
        while current:
            print current.data
            current = current.next


class LinkedList_tail(LinkedList):
    tail = None

    # O(1)
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    # O(n)
    def insertAfter(self, node, value):
        if not self.head:
            return

        current = self.head
        while current:
            if current == node:
                old_next = current.next
                new_node = Node(value)
                current.next = new_node
                new_node.next = old_next

                if new_node.next == None:
                    self.tail = new_node

                break

        node = node.next


class Double_linked_list(LinkedList_tail):

    # O(1)
    def insertAfter(self, node, value):
        if not self.head:
            return

        new_node = Node(value)
        new_node.next = node.next
        new_node.previous = node
        node.next = new_node

    # O(1)
    def delete(self, node):
        if not node:
            return

        # node is the head
        if not node.previous:
            self.head = node.next

        # node is the tail
        if not node.next:
            self.tail = node.previous

        if node.previous:
            node.previous.next = node.next

        if node.next:
            node.next.previous = node.previous

    # O(n)
    def reverseList(self):
        if not self.head:
            return

        #  head -> 0 -> 1 -> 2 -> 3 -> 4 ->none
        last_node = self.head  # 0
        current = self.head.next  # 1
        last_node.next = None
        self.tail = last_node # 0

        while current:  # 1 | 2 | 3 | ...
            next_node = current.next  # 2 | 3 | ...
            current.next = last_node  # 0 | 1 | ...
            last_node = current  # 1 | 2 | ...
            current = next_node # 2 | 3 | ...

        self.head = last_node


    def reverseRecursiveList(self, node):

        if not node.next:
            self.head = node
            return None

        self.reverseRecursivePrint(node.next)
        behind_node = node.next # node is the node before going into the call, so node.next is the node coming into the call
        behind_node.next = node # So here we are inverting the order of linking
        node.next = None








    def reverseRecursivePrint(self, node):

        if not node:
            return node

        self.reverseRecursivePrint(node.next)
        print node.data


def main():
    nodeList = Double_linked_list()

    for node in xrange(5):
        nodeList.append(node)

    # nodeList.printList()
    nodeList.reverseRecursiveList(nodeList.head)
    nodeList.printList()
    # nodeList.reverseRecursivePrint(nodeList.head)


main()
