class Node:

    #INICIA UM NODE COM UM DADO E UM POINTER
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    #INICIA UMA LISTA INICIALMENTE VAZIA
    def __init__(self): 
        self.head = None #HEAD INICIAL COMO NONE  


    #INSTANCIA UM NOVO NODE E APONTA PARA A HEAD
    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node #NOVO NODE VIRA A NOVA HEAD


    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)


    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)


    def print(self):
        if self.head is None: #SE NÃO HÁ HEAD NADA FOI ADICIONADO A LISTA
            print("Linked list is empty")
            return
        
        itr = self.head #INICIO NO POINTER DA HEAD
        llstr = '' #STRING ÚNICA CONTENDO TODOS OS DADOS
        while itr: #A PRIMEIRA HEAD SER NONE ME GARANTE O ULTIMO NEXT SER NONE
            llstr += str(itr.data) + ' --> '
            itr = itr.next #PERSIGO A LISTA
        print(llstr)

        
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    
    def removeLast(self):
        if self.head is None:
            raise Exception('List index out of range')
        itr = self.head
        while itr.next:
            previous = itr
            itr = itr.next
        previous.next = None


    def removeFirst(self):
        if self.head is None:
            raise Exception('List index out of range')
        self.head = (self.head).next


    def removeAt(self, index):
        lenght = self.getLength()
        if index > lenght:
            raise Exception("List index out of range.")
        elif index == lenght:
            self.removeLast()
            return
        elif index == 0:
            self.removeFirst()
        
        itr = self.head
        for i in range(index):
            previous = itr
            itr = itr.next
            following = itr.next if itr else None
        previous.next = following


    def insertAt(self, index, data):
        lenght = self.getLength()
        if lenght < index:
            raise Exception("List index out of range")
        elif index == 0:
            self.insertAtBeginning(data)
            return
        elif index == lenght:
            self.insertAtEnd(data)
            return
        itr = self.head
        for i in range(index):
            previous = itr
            itr = itr.next
        previous.next = Node(data, itr)
        
         
if __name__ == '__main__':

    #TESTE INSERT INICIO
    lL =  LinkedList()
    lL.insertAtBeginning(5)
    lL.insertAtBeginning(8)

    #TESTE INSERT FIM
    lL.insertAtEnd(7)
    lL.insertAtEnd(8)
    lL.print()

    #TESTE FRESH LIST
    lL.insertValues(['A', 'B', 'C', 'D'])
    lL.print()
    
    #TESTE LEN
    print(lL.getLength())

    #TESTE REMOVE
    lL.removeLast()
    lL.print()
    lL.removeAt(1)
    lL.print()
    lL.removeFirst()
    lL.print()

    #TESTE ADD
    lL.insertValues(['A', 'B', 'C', 'D'])
    lL.insertAt(3, 'C1')
    lL.print()