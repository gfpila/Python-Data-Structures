class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges: #CONVERTER TUPLAS PARA UM DICIONÁRIO RELACIONANDO POSSÍVEIS ROTAS
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]


    def getPath(self, start, end, path=[]):
        path = path + [start] #MANTER O TRACK DO ULTIMO NODE
        
        if start == end: #DESTINO MESMO QUE ORIGEM
            return [path]
        if start not in self.graphDict: #ORIGEM NÃO EXISTE
            return []
        
        paths = []
        
        for node in self.graphDict[start]:
            if node not in path:
                newPaths = self.getPath(node, end, path)
                for foundedPath in newPaths:
                    paths.append(foundedPath)
        
        return paths

if __name__ == '__main__':

    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]

    routeGraph = Graph(routes)
    print(routeGraph.getPath('Mumbai', 'Toronto'))