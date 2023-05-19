import heapq

class Graph_bestfs:
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed

    def print_path(self, path, goal):
        print("Path from {} to {}:".format(path[0], goal))
        for node in path:
            print(node, "->", end='')

    def bfs(self, start_node, goal_node, heuristic):
        visited = set()
        priority_queue = [(heuristic(start_node), start_node, [start_node])]  # (heuristic_value, node, path)

        while priority_queue:
            _, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path, goal_node

            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (heuristic(neighbor), neighbor, new_path))

        return None, goal_node, 0
