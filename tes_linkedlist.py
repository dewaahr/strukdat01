class mahasiswa:
    def __init__(self,nim,nama,ipk=None):
        self._nim   = nim
        self._nama  = nama
        self._ipk   = ipk

class Node:
    def __init__(self,element,n):
        self._element = element
        self._next = n

class SLLNC:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size = 0
    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addElementHead(self,e):
        baru = Node(e, None)
        if self.isEmpty()==True:
            self._head = baru
            self._tail = baru
            self._tail._next = None
        else:
            baru._next = self._head
            self._head = baru
            self._size += 1
        print("Data masuk head!")

    def printAll(self):
        if self.isEmpty()==False:
            bantu = self._head
            while(bantu!=None):
                print(bantu._element," ",end='')
                bantu = bantu._next
            print()
        else:
            print("Kosong")

 
a=SLLNC()
a.addElementHead('7122')
a.addElementHead('7123')
a.addElementHead('7124')
a.printAll()