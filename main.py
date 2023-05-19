import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.widgets import *
from PyQt5.QtWidgets import QMessageBox
import sys

# Importing searching algorithms
from bfs import Graph_bfs
from dfs import Graph_dfs
from astar import Graph_astar
from dls import Graph_dls
from ids import Graph_ids
from BFS import Graph_bestfs
from bds import Graph_bidirectional
from ucs import Graph_ucs
from sa import Graph_sa

DG = nx.DiGraph()
G = nx.Graph()

def initializeGraphs():
    # Initializing graph fo testing
    G.add_edge('S', 'A', weight=5)
    DG.add_edge('S', 'A', weight=5)

    G.add_edge('S', 'B', weight=9)
    DG.add_edge('S', 'B', weight=9)

    G.add_edge('S', 'D', weight=6)
    DG.add_edge('S', 'D', weight=6)

    G.add_edge('C', 'S', weight=6)
    DG.add_edge('C', 'S', weight=6)

    G.add_edge('A', 'B', weight=3)
    DG.add_edge('A', 'B', weight=3)
    DG.add_edge('B', 'A', weight=2)

    G.add_edge('B', 'C', weight=1)
    DG.add_edge('B', 'C', weight=1)

    G.add_edge('C', 'F', weight=7)
    DG.add_edge('C', 'F', weight=7)

    G.add_edge('D', 'C', weight=2)
    DG.add_edge('D', 'C', weight=2)

    G.add_edge('D', 'E', weight=2)
    DG.add_edge('D', 'E', weight=2)

    G.add_edge('E', 'G', weight=7)
    DG.add_edge('E', 'G', weight=7)

    G.add_edge('F', 'G', weight=8)
    DG.add_edge('F', 'G', weight=8)

    G.add_edge('F', 'D', weight=2)
    DG.add_edge('F', 'D', weight=2)


class Ui_AISearchingTechniquesMainWindow(object):
    counter = 0
    counterG = 0

    def __init__(self):
        self.heuristics = {'S': 5, 'A': 2, 'B': 1, 'C': 5, 'D': 2, 'E': 1, 'F': 2, 'G': 0}
        self.weights = {'SA': 5, 'SB': 9, 'SD': 6, 'AB': 3, 'BA': 2, 'BC': 1, 'CS': 6, 'CF': 7, 'DC': 2, 'DE': 2,
                        'EG': 7, 'FD': 2, 'FG': 8}
        self.start, self.goal = 'S', 'G'
        initializeGraphs()

    def GeneratePathClicked(self):
        original_stdout = sys.stdout  # Save a reference to the original standard output

        with open('test.txt', 'w') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            searchType = str(self.SearchTypecomboBox.currentText())
            graphType = str(self.GraphTypecomboBox.currentText())

            if graphType == "Undirectd Graph":
                if searchType == "BFS":
                    graphbfs = Graph_bfs(G, directed=False)
                    traced_path, goal = graphbfs.breadth_first_search(self.start, self.goal)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphbfs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(G, directed=False)
                    traced_path, goal = graphdfs.depth_first_search(self.start, self.goal)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphdfs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "DLS":
                    graphdls = Graph_dls(G, directed=False)
                    traced_path, goal = graphdls.depth_limited_search(self.start, self.goal, 1)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphdls.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "IDS":
                    graphids = Graph_ids(G, directed=False)
                    traced_path, goal = graphids.iterative_deepening_search(self.start, self.goal, 1)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphids.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "A*":
                    graphastar = Graph_astar(G, directed=False)
                    traced_path, cost, goal = graphastar.a_star_search(self.start, self.goal, self.getHeuristic,
                                                                       self.getCost)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphastar.print_path(traced_path, goal)
                        print('\nCost:', cost)
                    else:
                        self.pathNotFound()

                elif searchType == "BeFS":
                    graphBfs = Graph_bestfs(G, directed=False)
                    traced_path, goal = graphBfs.bfs(self.start, self.goal, self.getHeuristic)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphBfs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "BDS":
                    graphbds = Graph_bidirectional(G, directed=False)
                    traced_path, goal = graphbds.bidirectional_search(self.start, self.goal)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphbds.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "UCS":
                    graphucs = Graph_ucs(G, directed=False)
                    traced_path, goal = graphucs.ucs(self.start, self.goal, self.getCost)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphucs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "SA":
                    graphsa = Graph_sa(G, directed=False)
                    traced_path, goal = graphsa.simulated_annealing(self.start, self.goal, self.getHeuristic)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphsa.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

            else:
                if searchType == "BFS":
                    graphbfs = Graph_bfs(DG, directed=True)
                    traced_path, goal = graphbfs.breadth_first_search(self.start, self.goal)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphbfs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(DG, directed=True)
                    traced_path, goal = graphdfs.depth_first_search(self.start, self.goal)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphdfs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "DLS":
                    graphdls = Graph_dls(DG, directed=True)
                    traced_path, goal = graphdls.depth_limited_search(self.start, self.goal, 5)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphdls.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "IDS":
                    graphids = Graph_ids(DG, directed=True)
                    traced_path, goal = graphids.iterative_deepening_search(self.start, self.goal, 1)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphids.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "A*":
                    graphastar = Graph_astar(DG, directed=True)
                    traced_path, cost, goal = graphastar.a_star_search(self.start, self.goal, self.getHeuristic,
                                                                       self.getCost)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphastar.print_path(traced_path, goal)
                        print('\nCost:', cost)
                    else:
                        self.pathNotFound()

                elif searchType == "BeFS":
                    graphBfs = Graph_bestfs(DG, directed=True)
                    traced_path, goal = graphBfs.bfs(self.start, self.goal, self.getHeuristic)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphBfs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "BDS":
                    graphbds = Graph_bidirectional(DG, directed=True)
                    traced_path, goal = graphbds.bidirectional_search(self.start, self.goal)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphbds.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "UCS":
                    graphucs = Graph_ucs(DG, directed=True)
                    traced_path, goal = graphucs.ucs(self.start, self.goal, self.getCost)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphucs.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

                elif searchType == "SA":
                    graphsa = Graph_sa(DG, directed=True)
                    traced_path, goal = graphsa.simulated_annealing(self.start, self.goal, self.getHeuristic)
                    if traced_path:
                        self.PrintResults(traced_path)
                        print('Path:', end=' ')
                        graphsa.print_path(traced_path, goal)
                        print()
                    else:
                        self.pathNotFound()

        sys.stdout = original_stdout  # Reset the standard output to its original value

        with open("test.txt") as f:
            contents = f.read()

        self.TheResult_Label.setText(contents)

    def PrintResults(self, path):
        # changing nodes colors
        node_colors = {node: 'green' if node in path else 'blue' for node in G.nodes}
        node_colors[self.start], node_colors[self.goal] = 'yellow', 'red'

        if self.GraphTypecomboBox.currentText() == "Undirectd Graph":
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=1500, node_color=list(node_colors.values()))
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=nx.get_edge_attributes(G, 'weight'))
            nx.draw_networkx_nodes(G, pos, node_color=list(node_colors.values()))
            plt.show()
        elif self.GraphTypecomboBox.currentText() == "Directed Graph":
            pos = nx.spring_layout(DG)
            nx.draw(DG, pos, with_labels=True, node_size=1500, node_color=list(node_colors.values()))
            nx.draw_networkx_edge_labels(DG, pos, font_size=26, edge_labels=nx.get_edge_attributes(DG, 'weight'))
            nx.draw_networkx_nodes(G, pos, node_color=list(node_colors.values()))
            plt.show()

    def pathNotFound(self):
        # Create and configure the QMessageBox
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Path Not Found")
        message_box.setText("The specified path could not be found.")
        message_box.setStandardButtons(QMessageBox.Ok)

        # Display the message box
        message_box.exec_()

    def GenerateGraphClicked(self):
        if self.GraphTypecomboBox.currentText() == "Undirectd Graph":
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=nx.get_edge_attributes(G, 'weight'))
            plt.show()
        elif self.GraphTypecomboBox.currentText() == "Directed Graph":
            pos = nx.spring_layout(DG)
            nx.draw(DG, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(DG, pos, font_size=26, edge_labels=nx.get_edge_attributes(DG, 'weight'))
            plt.show()

    def AddNodeClicked(self):
        N1 = self.Node1_input.text()
        N2 = self.Node2_input.text()
        W = self.EdgeWieght_input.text()

        G.add_edge(N1, N2, weight=W)
        DG.add_edge(N1, N2, weight=W)
        self.weights[N1 + N2] = W   # Adding weights of edges to list used in algorithms

        self.counter = self.counter + 1
        self.Node1_input.clear()
        self.Node2_input.clear()
        self.EdgeWieght_input.clear()

    def HeuristicPushed(self):
        InputHeuristic = int(self.NodeHeuristic_input.text())
        InputNodeH = self.Node_Input.text()

        self.heuristics[InputNodeH] = InputHeuristic    # Adding heuristic to list used in algorithms
        self.Node_Input.clear()
        self.NodeHeuristic_input.clear()

    # These getters will be passed to algorithms so they can
    # access heuristics and weights of nodes and edges
    def getHeuristic(self, node):
        return self.heuristics[node]
    def getCost(self, node1, node2):
        if not self.weights.get(node1 + node2):
            return self.weights[node2 + node1]
        return self.weights[node1 + node2]

    def SubmitClicked(self):
        self.start = self.StartNode_input.text()
        self.goal = self.GoalNode_input.text()

        self.GoalNode_input.clear()
        self.StartNode_input.clear()

    def setupUi(self, AISearchingTechniquesMainWindow):
        AISearchingTechniquesMainWindow.setObjectName("AISearchingTechniquesMainWindow")
        AISearchingTechniquesMainWindow.resize(779, 790)
        self.centralwidget = QtWidgets.QWidget(AISearchingTechniquesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SearchTypecomboBox.setGeometry(QtCore.QRect(630, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SearchTypecomboBox.setFont(font)

        # To display names of all algorithms
        self.SearchTypecomboBox.setObjectName("SearchTypecomboBox")
        for i in range(9):
            self.SearchTypecomboBox.addItem("")

        self.GenerateGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateGraphButton.setGeometry(QtCore.QRect(630, 240, 131, 31))
        self.GenerateGraphButton.setObjectName("GenerateGraphButton")
        self.GenerateGraphButton.clicked.connect(self.GenerateGraphClicked)
        self.Node1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_input.setGeometry(QtCore.QRect(26, 48, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1_input.setFont(font)
        self.Node1_input.setText("")
        self.Node1_input.setObjectName("Node1_input")
        self.Node2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_input.setGeometry(QtCore.QRect(26, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2_input.setFont(font)
        self.Node2_input.setObjectName("Node2_input")
        self.Node1Label = QtWidgets.QLabel(self.centralwidget)
        self.Node1Label.setGeometry(QtCore.QRect(26, 25, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1Label.setFont(font)
        self.Node1Label.setObjectName("Node1Label")
        self.Node2Label = QtWidgets.QLabel(self.centralwidget)
        self.Node2Label.setGeometry(QtCore.QRect(26, 78, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2Label.setFont(font)
        self.Node2Label.setObjectName("Node2Label")
        self.EdgeWieghtLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdgeWieghtLabel.setGeometry(QtCore.QRect(26, 131, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieghtLabel.setFont(font)
        self.EdgeWieghtLabel.setObjectName("EdgeWieghtLabel")
        self.EdgeWieght_input = QtWidgets.QLineEdit(self.centralwidget)
        self.EdgeWieght_input.setGeometry(QtCore.QRect(26, 157, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieght_input.setFont(font)
        self.EdgeWieght_input.setObjectName("EdgeWieght_input")
        self.AddNodesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodesButton.setGeometry(QtCore.QRect(26, 189, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodesButton.setFont(font)
        self.AddNodesButton.setObjectName("AddNodesButton")
        self.AddNodesButton.clicked.connect(self.AddNodeClicked)
        self.TheResult_Label = QtWidgets.QLabel(self.centralwidget)
        self.TheResult_Label.setGeometry(QtCore.QRect(10, 280, 751, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TheResult_Label.setFont(font)
        self.TheResult_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.TheResult_Label.setLineWidth(2)
        self.TheResult_Label.setText("")
        self.TheResult_Label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.TheResult_Label.setObjectName("TheResult_Label")
        self.GeneratePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.GeneratePathButton.setGeometry(QtCore.QRect(460, 240, 131, 31))
        self.GeneratePathButton.setObjectName("GeneratePathButton")
        self.GeneratePathButton.clicked.connect(self.GeneratePathClicked)
        self.TheResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.TheResultLabel.setGeometry(QtCore.QRect(10, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TheResultLabel.setFont(font)
        self.TheResultLabel.setObjectName("TheResultLabel")
        self.Node_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node_Input.setGeometry(QtCore.QRect(227, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node_Input.setFont(font)
        self.Node_Input.setText("")
        self.Node_Input.setObjectName("Node_Input")
        self.NodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeLabel.setGeometry(QtCore.QRect(227, 26, 33, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeLabel.setFont(font)
        self.NodeLabel.setObjectName("NodeLabel")
        self.NodeHeuristicLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeHeuristicLabel.setGeometry(QtCore.QRect(227, 78, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristicLabel.setFont(font)
        self.NodeHeuristicLabel.setObjectName("NodeHeuristicLabel")
        self.NodeHeuristic_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NodeHeuristic_input.setGeometry(QtCore.QRect(227, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristic_input.setFont(font)
        self.NodeHeuristic_input.setObjectName("NodeHeuristic_input")
        self.AddNodeHeuristicButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodeHeuristicButton.setGeometry(QtCore.QRect(227, 130, 117, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodeHeuristicButton.setFont(font)
        self.AddNodeHeuristicButton.setObjectName("AddNodeHeuristicButton")
        self.AddNodeHeuristicButton.clicked.connect(self.HeuristicPushed)
        self.StartNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.StartNode_input.setGeometry(QtCore.QRect(430, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNode_input.setFont(font)
        self.StartNode_input.setText("")
        self.StartNode_input.setObjectName("StartNode_input")
        self.StartNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartNodeLabel.setGeometry(QtCore.QRect(430, 26, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNodeLabel.setFont(font)
        self.StartNodeLabel.setObjectName("StartNodeLabel")
        self.GoalNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.GoalNodeLabel.setGeometry(QtCore.QRect(430, 77, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNodeLabel.setFont(font)
        self.GoalNodeLabel.setObjectName("GoalNodeLabel")
        self.GoalNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalNode_input.setGeometry(QtCore.QRect(430, 100, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNode_input.setFont(font)
        self.GoalNode_input.setObjectName("GoalNode_input")
        self.GraphTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.GraphTypecomboBox.setGeometry(QtCore.QRect(630, 100, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(8)

        self.GraphTypecomboBox.setFont(font)
        self.GraphTypecomboBox.setObjectName("GraphTypecomboBox")
        self.GraphTypecomboBox.addItem("")
        self.GraphTypecomboBox.addItem("")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(430, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.SubmitClicked)
        AISearchingTechniquesMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AISearchingTechniquesMainWindow)
        self.statusbar.setObjectName("statusbar")
        AISearchingTechniquesMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AISearchingTechniquesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AISearchingTechniquesMainWindow)

    def retranslateUi(self, AISearchingTechniquesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AISearchingTechniquesMainWindow.setWindowTitle(
            _translate("AISearchingTechniquesMainWindow", "AI Searching Techniques"))
        self.SearchTypecomboBox.setCurrentText(_translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "DFS"))
        self.SearchTypecomboBox.setItemText(2, _translate("AISearchingTechniquesMainWindow", "DLS"))
        self.SearchTypecomboBox.setItemText(3, _translate("AISearchingTechniquesMainWindow", "IDS"))
        self.SearchTypecomboBox.setItemText(4, _translate("AISearchingTechniquesMainWindow", "A*"))
        self.SearchTypecomboBox.setItemText(5, _translate("AISearchingTechniquesMainWindow", "BeFS"))
        self.SearchTypecomboBox.setItemText(6, _translate("AISearchingTechniquesMainWindow", "UCS"))
        self.SearchTypecomboBox.setItemText(7, _translate("AISearchingTechniquesMainWindow", "BDS"))
        self.SearchTypecomboBox.setItemText(8, _translate("AISearchingTechniquesMainWindow", "SA"))

        self.GenerateGraphButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Graph"))
        self.Node1Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 1"))
        self.Node2Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 2"))
        self.EdgeWieghtLabel.setText(_translate("AISearchingTechniquesMainWindow", "Edge Weight"))
        self.AddNodesButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Nodes"))
        self.TheResult_Label.setWhatsThis(_translate("AISearchingTechniquesMainWindow",
                                                     "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.GeneratePathButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Path"))
        self.TheResultLabel.setText(_translate("AISearchingTechniquesMainWindow", "The Result"))
        self.NodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node "))
        self.NodeHeuristicLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node Heuristic"))
        self.AddNodeHeuristicButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Node Heuristic"))
        self.StartNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Start Node"))
        self.GoalNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Goal Nodes"))
        self.GraphTypecomboBox.setCurrentText(_translate("AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "Directed Graph"))
        self.SubmitButton.setText(_translate("AISearchingTechniquesMainWindow", "Submit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AISearchingTechniquesMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AISearchingTechniquesMainWindow()
    ui.setupUi(AISearchingTechniquesMainWindow)
    AISearchingTechniquesMainWindow.show()
    sys.exit(app.exec_())
