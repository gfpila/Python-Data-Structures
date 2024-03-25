class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None 

    
    def addChild(self, child):
        child.parent = self
        self.children.append(child)


    def removeChild(self, child):
        for element in self.children:
            if child == element:
                self.children.remove(element)


    def printNode(self, tabulation=0):
        indentation = "     " * tabulation
        print(indentation + self.data)
        for child in self.children:
            child.printNode(tabulation=tabulation + 1)
    

if __name__ == '__main__':
    
    #ROOT
    root = TreeNode('Eletronics')

    #LEVEL 1: Tipo produto
    laptop = TreeNode('Laptop')
    root.addChild(laptop)

    #LEVEL 2: Marca
    apple = TreeNode('Apple')
    laptop.addChild(apple)

    #LEVEL 3: Produto
    macBookAir = TreeNode('MacBook Air')
    apple.addChild(macBookAir)

    #Mais adições
    smartphone = TreeNode('Smartphone')
    samsung = TreeNode('Samsung')
    motorola = TreeNode('Motorola')
    galaxyS24 = TreeNode('Galaxy S24')
    motoE22 = TreeNode('Moto E22')
    root.addChild(smartphone)
    smartphone.addChild(motorola)
    smartphone.addChild(samsung)
    motorola.addChild(motoE22)
    samsung.addChild(galaxyS24)

    #PRINT
    root.printNode()

    #TESTE REMOVE
    print('\nRemovendo smartphone...\n')
    root.removeChild(smartphone)
    root.printNode()