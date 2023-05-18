class Graph_dls:
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed

    def depth_limited_search(self, start_node, goal_node, depth):
        visited = []
        queue = []

        visited.append(start_node)
        queue.append((start_node, [start_node]))

        while queue:
            node, path = queue.pop()

            # if goal found stop loop
            if node == goal_node:
                return path, goal_node

            if len(path) == depth:
                return None, goal_node

            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
                    visited.append(neighbor)

                    if not self.directed:
                        visited.append(neighbor)  # Mark as visited from the neighbor side if the graph is undirected

        return None, goal_node

    def print_path(self, path, goal):
        print("Path from {} to {}:".format(path[0], goal))
        for node in path:
            print(node, " -> ", end=' ')
