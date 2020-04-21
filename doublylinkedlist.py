class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
        self.__before=None
    def set_data(self,data):
        self.__data=data
    def get_data(self):
        return self.__data
    def set_next(self,newnode):
        self.__next=newnode
    def get_next(self):
        return self.__next
    def set_before(self,newnode):
        self.__before = newnode
    def get_before(self):
        return self.__before
class Linkedlist:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def lengthoflist(self):
        length = 0
        if (self.__head == None):
            return length
        else:
            lastnode = self.__head
            while lastnode is not None:
                length += 1
                lastnode = lastnode.get_next()
            return length
    def addnode(self,data):
        newnode=Node(data)
        if(self.__head==None):
            self.__head=self.__tail=newnode
        else:
            self.__tail.set_next(newnode)
            temp=self.__tail
            self.__tail=self.__tail.get_next()
            self.__tail.set_before(temp)
    def addnodestart(self,data):
        newnode=Node(data)
        if self.__head is None:
            self.__head=self.__tail=newnode
        else:
            newnode.set_next(self.__head)
            self.__head.set_before(newnode)
            self.__head=self.__head.get_before()
    def deletenode(self):
        if(self.__head==None):
            print("No Elements Present to Delete")
        elif(self.__head==self.__tail):
            self.__head=self.__tail
        lastnode=self.__head
        while lastnode.get_next() is not None:
            prevnode=lastnode
            lastnode=lastnode.get_next()
        lastnode.set_before(None)
        prevnode.set_next(None)
        self.__tail=prevnode
    def deletenodestart(self):
        if self.__head is None:
            print("No Elements Present to Delete")
        elif(self.__head==self.__tail):
            self.__head=self.__tail=None
        temp=self.__head
        self.__head=self.__head.get_next()
        self.__head.set_before(None)
        temp.set_next(None)
    def deletenodebefore(self,data):
        if(self.__head is None or self.__head==self.__tail or self.__head.get_data()==data):
            print("No Elements to Delete")
            return
        currentnode=self.__head
        while currentnode is not None:
            if(currentnode.get_data()==data):
                temp=prevnode.get_before()
                if temp!=None:
                    temp.set_next(currentnode)
                    currentnode.set_before(temp)
                    prevnode.set_before(None)
                    prevnode.set_before(None)
                else:
                    self.__head=self.__head.get_next()
                    prevnode.set_next(None)
                    currentnode.set_before(None)
                return
            prevnode=currentnode
            currentnode=currentnode.get_next()
        print("No Node Found")
    def displaynodeforward(self):
        if(self.__head is None):
            print("The Linkedlist is Empty")
        else:
            lastnode=self.__head
            while lastnode is not None:
                print(lastnode.get_data())
                lastnode=lastnode.get_next()

    def displaynodereverse(self):
        if(self.__head==None):
            print("No Elements to Print")
        else:
            lastnode=self.__tail
            while lastnode is not None:
                print(lastnode.get_data())
                lastnode=lastnode.get_before()

c=Linkedlist()
c.addnode(1)
c.addnode(2)
c.addnode(3)
c.addnode(4)
c.addnode(5)
c.addnode(6)
c.addnode(7)
c.addnodestart(0)
c.displaynodereverse()
c.deletenodestart()
c.deletenode()
c.deletenodebefore(1)
c.displaynodeforward()
