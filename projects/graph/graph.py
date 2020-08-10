"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex Does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex)

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push a starting vertex
        s = Stack()
        s.push(starting_vertex)

        # create a set to store the visited vertices
        visited = set()

        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    # Pass a visited=None because visited will be updated, so we cannot set in our function
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Check if are visited is updated
        if visited is None:
            # If not then update it to the set method
            visited = set()

        # Check if the starting vertex has not been visited
        if starting_vertex not in visited:
            # If not then add it onto visited
            visited.add(starting_vertex)
            # Print out the starting vertex for debugging
            print(starting_vertex)

            # Iterate through the neighbors of the starting vertex
            for neighbor in self.get_neighbors(starting_vertex):
                # Use recursion to cycle through the neighbors passing the neighbor and visited
                self.dft_recursive(neighbor, visited)
        else:
            # When all neighbors have been visited then just return None
            return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue and enqueue containing our starting_vertex index
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a set to store the visited vertices
        visited = set()

        # Check if the queue is not empty
        while q.size() > 0:
            # Dequeue the first path in the queue
            path = q.dequeue()

            # Grab the last_vertex in our path
            last_vertex = path[-1]

            # If our last_vertex is never visited then add it to visited
            if last_vertex not in visited:
                visited.add(last_vertex)

            # Check if our last_vertex is at our destination
            if last_vertex == destination_vertex:
                # If it is then return the path
                return path

            # Iterate through the neighbors in our last_vertex
            for neighbor in self.get_neighbors(last_vertex):
                # Create a new path for the enqueue
                new_path = path + [neighbor]
                # Enqueue our new_path
                q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # Create an empty stack and push a starting_vertex
        s = Stack()
        s.push([starting_vertex])

        # Create a set to store the visited vertices
        visited = set()

        # Check if the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            path = s.pop()

            # Grab the last_vertex in our path
            last_vertex = path[-1]

            # If our last_vertex is never visited then add it to visited
            if last_vertex not in visited:
                visited.add(last_vertex)

            # Check if our last_vertex is at our destination
            if last_vertex == destination_vertex:
                return path

            # Iterate through the neighbors in our last_vertex
            for neighbor in self.get_neighbors(last_vertex):
                # Create a new path for the enqueue
                new_path = path + [neighbor]
                # Enqueue our new_path
                s.push(new_path)

    # Pass a visited=None and path=None because visited and path will be updated, so we cannot set in our function
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """

        # Check if our visited is empty
        if visited == None:
            # If it is then assign it to set for visited vertices
            visited = set()

        # Check if our starting_vertex is not in our visited
        if starting_vertex not in visited:
            # If it is not then add it onto our visited
            visited.add(starting_vertex)

        # Check if path is empty
        if path == None:
            # If it is then set it to an empty array
            path = []

        # Create a new path adding on our current path and the starting_vertex
        path = path + [starting_vertex]

        # Check if we have reached our destination and have gone through the path
        if starting_vertex == destination_vertex:
            # If we have then return path
            return path

        # Iterate through the neighbors in the starting_vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # Check if the neighbor is visited
            if neighbor not in visited:
                # Assign our new_path to our recursive function
                new_path = self.dfs_recursive(neighbor, destination_vertex,
                                              visited, path)
                # Check if our new_path is not empty
                if new_path is not None:
                    # If not then return it
                    return new_path

        # Base case to show all neighbors have been visited
        return None


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
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
    print(graph.dfs_recursive(1, 6))
