from collections import deque


class Graph_astar:
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed

    def depth_first_search(self, start_node, goal_node):
        visited = set()
        queue = deque([(start_node, [], 0)])  # Include cumulative weight in the queue
        visited.add(start_node)

        while queue:
            node, path, weight = queue.pop()
            path = path + [node]

            if node == goal_node:
                return path, goal_node  # Return the path and cumulative weight if the goal node is reached

            for neighbor, edge_weight in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path, weight + edge_weight))
                    visited.add(neighbor)

                    if not self.directed:
                        visited.add(neighbor)  # Mark as visited from the neighbor side if the graph is undirected

        return None, goal_node

    def print_path(self, path, goal):
        print("Path from {} to {}:".format(path[0], goal))
        for node in path:
            print(node, " -> ", end=' ')
