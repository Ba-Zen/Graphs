"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            raise IndexError("Can not create edge case based on given vertices")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Create list of visited nodes
        visited = set()
        # Put starting node in the queue
        q.enqueue(starting_vertex)
        # While: queue not empty
        while q.size() > 0:
            # Pop first node out of queue
            vertex = q.dequeue()
            # If not visited
            if vertex not in visited:
                visited.add(vertex)
                print("BFT",vertex)
        #     Mark as visited
        #     Get adjacent edges and add to back of queue
                for next_vert in self.vertices[vertex]:
                    q.enqueue(next_vert)
        #     Go to top of loop

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                visited.add(vertex)
                print("DFT", vertex)
                for next_vert in self.vertices[vertex]:
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Check if visited is None. If None initalize empty set
        if visited is None:
            visited = set()
        # If node not visited:
        if starting_vertex not in visited:
            # Mark node visited
            visited.add(starting_vertex)
            #print("DFT_RECURSIVE", starting_vertex)
            # then call dft_recursive on each
            for next_vert in self.vertices[starting_vertex]:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty Queue and enqueue path to starting_vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # Create empty set to store visted nodes
        visited = set()
        # While queue is not empty:
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # get vertex from end of path
            v = path[-1]
            # if vertex = target
            if v == destination_vertex:
                #return path
                return path
            # if the vertex has not been visited
            if v not in visited:
                # mark it visted
                visited.add(v)
                # then add a path to all adjacent vertices to back of queue
                for next_vert in self.vertices[v]:
                    # copy path
                    path_copy = list(path)
                    # append next vert to back of copy
                    path_copy.append(next_vert)
                    # enqueue copy
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # Create an empty Stack and push path to starting_vertex
        s = Stack()
        s.push([starting_vertex])
        # Create empty set to store visted nodes
        visited = set()
        # While stack is not empty:
        while s.size() > 0:
            # Pop the first path offa stack
            path = s.pop()
            # get vertex from end of path
            v = path[-1]
            # if vertex = target
            if v == destination_vertex:
                #return path
                return path
            # if the vertex has not been visited
            if v not in visited:
                # mark it visted
                visited.add(v)
                # then add a path to all adjacent vertices to back of queue
                for next_vert in self.vertices[v]:
                    # copy path
                    path_copy = list(path)
                    # append next vert to back of copy
                    path_copy.append(next_vert)
                    # push copy onto the stack
                    s.push(path_copy)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
