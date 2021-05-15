class Node(object):

    def __init__(self,name):
        self.name = name
        self.adjacencyLists = []
        self.visited = False
        self.predecessor = None


class DepthFirstSearch(object):

    def dfs(self, startNode):

        startNode.visited = True
        print("%s" % startNode.name)

        for n in startNode.adjacencyLists:
            if not n.visited:
                self.dfs(n)



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyLists.append(node3)
node1.adjacencyLists.append(node5)
node3.adjacencyLists.append(node4)
node4.adjacencyLists.append(node2)

dfs = DepthFirstSearch()
dfs.dfs(node1)


