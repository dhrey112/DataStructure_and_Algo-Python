class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


class CircularLinkedList:
    def __init__(self):
        self.head = None 

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head 
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next 
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None 
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next 
                        cur = cur.next

    # Count the length of a circular linked list
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    # the split_list method
    def split_list(self):
        size = len(self)    

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head 

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    # Remove entire node
    def remove_node(self, key):
        if self.head:
            if self.head == key:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next 
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None 
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next
                    if cur == key:
                        prev.next = cur.next 
                        cur = cur.next

    # Josephus Problem
    def josephus_circle(self, step):
        cur = self.head 

        length = len(self)
        while length > 1:
            count = 1 
            while count != step:
                cur = cur.next 
                count += 1
            print("KILL:" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            length -= 1

    # Is Circular Linked List
    def is_circular_linked_list(self, input_list):
        if input_list.head:
            cur = input_list.head
            while cur.next:
                cur = cur.next
                if cur.next == input_list.head:
                    return True
            return False
        else:
            return False

    
if __name__ == '__main__':
    cllist = CircularLinkedList()
    print("Creating")
    cllist.append("C")
    cllist.append("D")
    cllist.prepend("B")
    cllist.prepend("A")
    cllist.print_list()

    print('\nAfter Removing')
    cllist.remove("A")
    cllist.remove("C")
    cllist.print_list()

    # A -> B -> C -> D -> ...
    # A -> B -> ... and C -> D -> ...
    print('\nSpliting')
    # cllist = CircularLinkedList()
    cllist.append("A")
    cllist.append("B")
    cllist.append("C")
    cllist.append("D")
    cllist.append("E")
    cllist.append("F")

    cllist.split_list()
    print('\nJosephus Problems')

    jllist = CircularLinkedList()
    jllist.append(15)
    jllist.append(2)
    jllist.append(3)
    jllist.append(4)


    jllist.josephus_circle(2)
    jllist.print_list()
    print()

    cllist = CircularLinkedList()
    cllist.append(1)
    cllist.append(2)
    cllist.append(3)
    cllist.append(4)

    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    print(cllist.is_circular_linked_list(cllist))
    print(cllist.is_circular_linked_list(llist))
                        