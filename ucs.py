import heapq


class Graph_ucs:
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed

    def print_path(self, path, goal):
        print("Path from {} to {}:".format(path[0], goal))
        for node in path:
            print(node, "->", end='')

    def ucs(self, start_node, goal_node, weight):
            return self.uniform_cost_search_undirected(start_node, goal_node, weight)

    def uniform_cost_search_undirected(self, start_node, goal_node, weight):
        visited = set()
        priority_queue = [(0, start_node, [start_node])]  # (cumulative_cost, node, path)

        while priority_queue:
            cumulative_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path, goal_node

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    new_cumulative_cost = cumulative_cost + weight(current_node, neighbor)
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cumulative_cost, neighbor, new_path))

        return None, goal_node
