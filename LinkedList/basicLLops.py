class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def traverse(self):
        current=self.head
        while current.next!=None:
            print(current.val)
            current=current.next
        print(current.val)
        return
    def append(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=Node(data)
        return
    def insertinmid(self,prev,data):
        if prev==None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            second_half=prev.next
            prev.next=new_node
            new_node.next=second_half
        return
    def addatfront(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        return
    def deleteval(self,data):
        current=self.head
        prev=None
        while current.val!=data:
            prev=current
            current=current.next
        if prev==None:
            self.head=current.next
        else:
            prev.next=current.next
        return
    def deletetatposition(self,position):
        current=self.head
        pos=1
        if position==1:
            self.head=current.next
        else:
            while pos<position :
                prev=current
                current=current.next
                pos+=1
            prev.next=current.next
        return
    def length(self):
        current=self.head
        count=1
        while current.next!=None:
            current=current.next
            count+=1
        return count
    def reversingList(self):
        prev=None
        current=self.head
        while current!=None:
            n=current.next
            current.next=prev
            prev=current
            current=n
        self.head=prev
        return
