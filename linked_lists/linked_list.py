class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None

    # Insert node at the beginning
    def insert_at_begining(self, data):
        node1 = node(data, self.head)
        self.head = node1

    # Print the linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        ll_str = ''

        while itr:
            ll_str += str(itr.data) + '-->'
            itr = itr.next

        print(ll_str)

    # Insert Node at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node(data, None) 

    # Insert a mini-linked list inside the bigger one
    def insert_values(self, data_list):
        if self.head == None:
            self.head = node(data_list[0], None) 
            
            for i in range(1, len(data_list)):
                self.insert_at_end(data_list[i])

        for data in data_list:
                self.insert_at_end(data)

    # Get the length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        print("The length of linkedlist:", count)

    def remove_at(self, index):
        if index<0: #'or index>=self.get_length():' <-- This statement gave me random error
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next 
            #Shouldn't worry about the lost head because
            #the python has automatic garbage collector
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    # Insert a node at the given index
    def insert_at(self, index, data):
        if index<0:
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node1 = node(data, itr.next)
                itr.next = node1
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = linkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(69)
    ll.insert_at_end(6969)
    ll.insert_at_begining(696)
    ll.insert_at_end(69696969)
    ll.insert_values(["Mango", "Banana", "grapes"])
    ll.print()
    ll.insert_at(3, "jackfruit")
    ll.remove_at(2)
    ll.print()
    ll.get_length()