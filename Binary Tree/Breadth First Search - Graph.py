class Node(object):

    def __init__(self,name):
        self.name = name
        self.adjacencyLists = []
        self.visited = False
        self.predecessor = None


class BreadthFirstSearch(object):

    def bfs(self, startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:

            actualnode = queue.pop(0)
            print("%s" % actualnode.name)

            for n in actualnode.adjacencyLists:
                if not n.visited:
                    n.visited= True
                    queue.append(n)



node1 = Node("A")
node2 = Node("B")
node3 = Node("c")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyLists.append(node3)
node1.adjacencyLists.append(node5)
node3.adjacencyLists.append(node4)
node4.adjacencyLists.append(node2)

bfs = BreadthFirstSearch()
bfs.bfs(node1)


