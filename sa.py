import math
import random


class Graph_sa:
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed

    def simulated_annealing(self, start, goal, heuristic):
        temp = 1
        currentNode = start
        bestHeuristic = heuristic(start)
        path = []

        while temp > 0.001:
            path.append(currentNode)
            # select a random neighbor and visit it
            neighbours = list(self.graph.neighbors(currentNode))
            currentNode = random.choice(neighbours)

            if currentNode == goal:
                return path, goal

            tempHeuristic = heuristic(currentNode)
            deltaE = bestHeuristic - tempHeuristic
            # Simulated annealing
            if deltaE < 0:
                bestHeuristic = tempHeuristic
            else:
                probability = math.exp(deltaE / temp)
                if probability > random.uniform(0, 1):
                    bestHeuristic = tempHeuristic
            temp *= 0.95

        return None, goal

    def print_path(self, path, goal):
        print("Path from {} to {}:".format(path[0], goal))
        for node in path:
            print(node, " -> ", end=' ')
