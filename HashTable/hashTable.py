class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] #Popular um array com o número de buckets
        self.slots = 100

    
    def getHash(self, key):
        h = 0
        for char in key: #Somar todos os valores ASCII da string
            h += ord(char)
        return h % self.MAX #Retornar o resto dividido pelo tamanho
    
    
    def addKey(self, key):
        if self.slots == 0:
            raise Exception('The hash table is full for this Key.')
        hash = self.getHash(key)
        if self.arr[hash] != None:
            raise Exception('Key already exists.')
        else:
            self.arr[hash] = [key]
            self.slots -= 1

    
    def removeKey(self, key):
        hash = self.getHash(key)
        if self.arr[hash] == None:
            raise Exception('Key not found.')
        else:
            self.arr[hash] = None
            self.slots += 1


    def __setitem__(self, key, value):
        hash = self.getHash(key)
        if self.arr[hash] == None:
            self.addKey(key)
            self.arr[hash].append(value)
        else:
            self.arr[hash].append(value)


    def addElements(self, key, dataList):
        hash = self.getHash(key)
        if self.arr[hash] == None:
            self.addKey(key)
            for data in dataList:
                self.arr[hash].append(data)
        else:
            for data in dataList:
                self.arr[hash].append(data)


    def removeElement(self, key, value):
        hash = self.getHash(key)
        if self.arr[hash] == None:
            raise Exception('Key not found.')
        if value in self.arr[hash]:
            self.arr[hash].remove(value)
        else:
            raise Exception("Value not found")
        
        
    def removeElements(self, key, dataList):
        hash = self.getHash(key)
        if self.arr[hash] == None:
            raise Exception('Key not found.')
        for data in dataList:
            if data in self.arr[hash]:
                self.arr[hash].remove(data)
            else:
                raise Exception(f"Value {data} not found")
            
        
    def __getitem__(self, key):
        hash = self.getHash(key)
        if self.arr[hash] == None:
            raise Exception("Key not found")
        else:
            return self.arr[hash][1:]
        

    def print(self):
        for element in self.arr:
            if element is not None:
                print(f'{element[0]}: {element[1:]}')

        
if __name__ == '__main__':

    #TESTE ADD
    hashMap = HashTable()
    hashMap['march 6'] = 3
    hashMap['march 9'] = 9
    hashMap['march 10'] = [1, 2, 3]
    hashMap.addElements('march 10', [4,5,6])
    hashMap.print()

    
    myElements = hashMap['march 10']
    print(myElements)

    #TESTE REMOVE
    hashMap.removeElement('march 6', 3)
    hashMap.removeKey('march 9')
    hashMap.removeElements('march 10', [4,5,6])
    hashMap.print()