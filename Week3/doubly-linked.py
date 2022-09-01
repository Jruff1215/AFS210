class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        node = Node(data)
        if (self.head == None):
            self.head = node
            self.count += 1
            return
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.count += 1



    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.count += 1

            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node
            node.prev = temp
            self.tail = node
            self.count += 1

  

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        node = Node(data)
        counter = 0
        if index == self.count:
            self.addLast(data)
        elif index > self.count:
            return "Out of Bounds!"
        elif index == 0:
            self.addFirst(data)
        else:
            temp = self.head
            while(temp.next != None and counter < index):
                temp = temp.next
                counter += 1
            next = temp.next
            temp.next = node
            node.prev = temp
            next.prev = node
            node.next = next
            self.count += 1
            # print(temp.data)
            
    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        node = Node(data)
        counter = 0
        temp = self.head
        while(temp.next != None and temp.data != data):
            temp = temp.next
            counter += 1
        # print(temp.data, counter)
        print(counter)
        return counter
        


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)
        

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

dblList = DoublyLinkedList()
dblList.addFirst('May')
dblList.add('the')
dblList.addLast('Force')
dblList.addLast('be')
dblList.addLast('with')
dblList.addLast('you')
dblList.addLast('!')
print(dblList)
print('---------------------------------')

dblList.indexOf('with')
print('---------------------------------')

dblList.addAtIndex('us', 4)
dblList.addAtIndex('all', 6)
dblList.deleteAtIndex(6)
# print(dblList.__str__())
print(dblList)

