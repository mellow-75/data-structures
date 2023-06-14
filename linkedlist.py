class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head=None


    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linked list empty")
            return

        itr=self.head
        llstr=''

        while itr:

            llstr+=str(itr.data)+'-->'
            itr=itr.next

        print(llstr)



    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data, None)


    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count



    def remove_at(self, index):
        if index<0 or index>= self.get_length():
            raise Exception('invalid index')

        if index==0:
            self.head=self.head.next
            return

        count=0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1



    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('invalid index')

        if index==0:
            self.insert_at_begining(data)

            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1




#                **********exercise*******************
    def get_pos(self,data):
        itr=self.head
        count=0
        while itr:
            if data==itr.data:
                return count
                break
            count += 1
            itr=itr.next




    def insert_after_value(self,data_after,data_to_insert):

        idx=self.get_pos(data_after)
        idx+=1
        self.insert_at(idx,data_to_insert)








    def remove_by_value(self, data):
        idx=self.get_pos(data)
        self.remove_at(idx)




class doubleNode:
    def __init__(self,prev,data,next):
        self.prev=prev
        self.data=data
        self.next = next


class doublylinkedlist:
    def __init__(self):
        self.head=None

    def print_forward(self):
        if self.head==None:
            print("empty list")
            return

        itr=self.head
        llstr=" "
        llstr+= str(itr.data)+str(itr.next)+"--->"
        itr=itr.next
        while itr.next:
            llstr+=str(itr.prev)+str(itr.data)+str(itr.next)+"--->"
            itr=itr.next

        print(llstr)











ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
idx=ll.get_pos("grapes")
print(idx)
len=ll.get_length()
print(len)
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print()
ll.remove_by_value("orange")  # remove orange from linked list
ll.print()

ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()