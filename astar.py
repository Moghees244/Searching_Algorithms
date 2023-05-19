import heapq


class Graph_astar:
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed

    def a_star_search(self, start_node, goal_node, heuristic, cost_function):
            return self.astar_undirected(start_node, goal_node, heuristic, cost_function)

    def astar_undirected(self, start_node, goal_node, heuristic, cost_function):
        visited = set()
        priority_queue = [(0 + heuristic(start_node), 0, start_node, [start_node])]  # (f_value, g_value, node, path)

        while priority_queue:
            _, g_value, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path, goal_node

            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_g_value = g_value + cost_function(current_node, neighbor)
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_g_value + heuristic(neighbor), new_g_value, neighbor, new_path))

        return None, goal_node

    def print_path(self, path, goal):
        print("Path from {} to {}:".format(path[0], goal))
        for node in path:
            print(node, " -> ", end=' ')
