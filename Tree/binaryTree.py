class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def addChild(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left: #PERCORRER RECURSIVAMENTE  ATÉ ENCONTRAR UM LEFT VAZIO
                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)
                
            
    def traversal(self):
        elements = []

        #LEFT TREE:
        if self.left:
            elements += self.left.traversal()

        #BASE NODE:
        elements.append(self.data)

        #RIGHT TREE:
        if self.right:
            elements += self.right.traversal()
            
        return elements
    

    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data and self.left:
            return self.left.search(value)
        elif value > self.data and self.right:
            return self.right.search(value)
        
        return False

    
    
def buildTree(elements):
    root = BinaryTree(elements[0])
    for data in elements[1:]:
        root.addChild(data)
    return root

if __name__ == "__main__":
    elements = [17, 16, 17, 1, 20, 9, 2, 18, 57, 24, 16]
    myTree = buildTree(elements)
    print(myTree.traversal())

    #TESTE SEARCH
    print(myTree.search(18))