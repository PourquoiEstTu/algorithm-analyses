from collections import deque
import random
import copy
import matplotlib.pyplot as plot
from itertools import combinations

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        print(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    #print(marked)
                    return True
                S.append(node)
    #print(marked)
    return False

#Depth first search path return
def DFS2(G, node1, node2):
    if G.adj[node2] == []: return []
    S = [node1]
    marked = {}
    path = []
    counter = -1
    found = False
    for node in G.adj:
        marked[node] = False #initialize marked dictionary to false 
    while len(S) != 0:
        #print(S)
        #print(marked)
        current_node = S.pop() #take/remove last element of S
        #print(current_node)
        #print(path)
        #print(" ")
        if not marked[current_node]: #check element if not marked
            marked[current_node] = True #mark element
            path.append(current_node)
            for node in G.adj[current_node]: #for each node adjacent to current_node
                if node == node2: #check if correct node found
                    path.append(node)
                    #print(S)
                    if path[0] != node1: return [node1] + path
                    else: return path
                if (not marked[node]): 
                    counter += 1
                    S.append(node) #add adjancent nodes to S 
                    found = True
            if not found and len(S) != 0: 
                for x in range(0, counter):
                    path.remove(path[len(path) - 1])
            found = False
    #print(marked)
    return []

#DFS to find all paths from node1, potentially works
def DFS3(G, node1):
    pre = {}
    keys = []
    for elm in G.adj.keys():
        if not (elm == node1):
            keys.append(elm)
    for node in keys: #for each node other than node1
        x = DFS2(G, node1, node)
        #print(x)
        if not len(x) == 0:
            pre[node] = len(x) - 1
    return pre

#BFS path return implementation
def BFS2(G, node1, node2):
    # not sure if below is correct
    # if node1 == node2 :
    #     return [node1]
    Q = deque([node1])
    pathList = []
    breakVar = False
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        pathList.append(current_node)
        # num_of_adj_nodes = len(G.adjacent_nodes(current_node))
        # num_of_marks = 0 
        # print("Current node: " + str(current_node))
        # print("Number of adjacent nodes to current_node: " + str(num_of_adj_nodes))
        for node in G.adj[current_node]:
            if node == node2:
                pathList.append(node2)
                breakVar = True
                break 
            if not marked[node]:
                # print("Marked node: " + str(node))
                Q.append(node)
                marked[node] = True
        if breakVar :
            break
        # print(pathList)
    if pathList[len(pathList) - 1] != node2 :
        return []
    # for i in range(1, len(pathList) - 2) :
    #     # print(pathList[i])
    #     if (pathList[i - 1] not in G.adjacent_nodes(pathList[i])) or (pathList[i+1] not in G.adjacent_nodes(pathList[i])) :
    #         # print(pathList[i])
    #         pathList.pop(i)

    return pathList


#Depth First Search
def editedDFS(G, node1) :
    S = [(node1, -1)]
    marked = {}
    for i in G.adj :
        marked[i] = False
    while len(S) != 0:
        tuple = S.pop()
        current_node0 = tuple[0]
        current_node1 = tuple[1]
        # print("current_node: " + str(current_node))
        # print("colour of current_node: " + str(marked[current_node]))
        for node in G.adj[current_node0] :
            if not marked[node] :
                S.append((node, current_node0))
                marked[node] = True
                    # print("adjacent node: " + str(node))
                    # print("adjacent node mark: " + str(marked[node]))
            elif node != current_node1 :
                return True
    #print(marked)
    return False

def has_cycle(G):
    for i in G.adj :
        if editedDFS(G, 1) :
            return True
    return False
# test code for has_cycle
#  generates graph in the lab description
# g = Graph(7)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.add_edge(3, 5)
# g.add_edge(4, 5)
# g.add_edge(4, 6)
# print("Final edgeTo list:" + str(BFS2(g, 1, 1)))
# print(has_cycle(g))
# print(DFS(g, 1, 1))

# g1 = Graph(7)
# g1.add_edge(0, 1)
# g1.add_edge(0, 2)
# g1.add_edge(0, 5)
# g1.add_edge(1, 2)
# g1.add_edge(2, 3)
# g1.add_edge(2, 4)
# g1.add_edge(3, 4)
# g1.add_edge(3, 5)
# g1.add_edge(3, 6)
# # print("test paths: " + str(BFS2(g1, 0, 0)))
# print(has_cycle(g1))

def is_connected(G):
    path = {}
    for elm in G.adj.keys():
        if not (DFS3(G, elm) == path):
            return True
    return False

# precondition: nodes cannot be numbered with negative integers
def BFS3(G, targetNode):
    pred_dict = {}
    count = 0
    for i in G.adj :
        count += 1
    edgeTo = [-1] * count
    Q = deque([targetNode])
    marked = {targetNode : True}
    for node in G.adj:
        if node != targetNode:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                # print(edgeTo)
                edgeTo[node] = current_node
                Q.append(node)
                marked[node] = True
    for i in range(len(edgeTo)) :
        if (edgeTo[i] != (-1) ) :
            pred_dict[i] = edgeTo[i]
    return pred_dict

#Use the methods below to determine minimum vertex covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

# Approx algorithms
def approx1(G):
    C = []
    Gc = Graph(G.number_of_nodes())
    Gc.adj = copy.deepcopy(G.adj) #copy graph
    while not is_vertex_cover(Gc, C): #until vertex cover is found
        max = 0
        for x in Gc.adj.keys(): #find max vertex in graph
            if len(Gc.adj[x]) > len(Gc.adj[max]):
                max = x
        C.append(max) #add max vetex to C
        for z in Gc.adj[max]: #remove all connections to max
            Gc.adj[z].remove(max)
        Gc.adj[max] = [] #remove all connections from max
    # print(C)
    return C

def approx2(G):
    C = []
    while not is_vertex_cover(G, C): #until vertex cover is found
        ranNum = random.randint(0, G.number_of_nodes() - 1) #random vertex from graph
        if not ranNum in C: #add to C if not already in C
            C.append(ranNum)
    # print(C)
    return C

def approx3(G):
    C = []
    mark = True
    Gc = Graph(G.number_of_nodes())
    Gc.adj = copy.deepcopy(G.adj)
    while not is_vertex_cover(Gc, C): #until vertex cover is found
        u = random.randint(0, Gc.number_of_nodes() - 1) #get random vertex
        if not (Gc.adj[u] == []): #if it has adjacent nodes, choose a random one
            v = random.choice(Gc.adj[u])
            C.append(u)
            C.append(v) #add u and v to C
            for z in Gc.adj[u]: #remove all connectsion to u
                Gc.adj[z].remove(u)
            Gc.adj[u] = [] #remove all connections from u
            for q in Gc.adj[v]: #remove all connections to v
                Gc.adj[q].remove(v)
            Gc.adj[v] = [] #remove all connections from v
    # print(C)
    return C

# # test code for BFS3
# #  generates graph in the lab description
# g = Graph(7)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.add_edge(3, 5)
# g.add_edge(4, 5)
# g.add_edge(4, 6)
# print("Final edgeTo list:" + str(BFS3(g, 1)))

# Test code for when dfs wasn't working right
# g = Graph(6)
# g.add_edge(0,2)
# g.add_edge(0,1)
# g.add_edge(0,3)
# g.add_edge(2,4)
# g.add_edge(2,3)
# g.add_edge(3,5)
# print(DFS(g, 0, 0))
def create_random_graph(i, j):
    G = Graph(i + 1)
    L = []
    t = 0
    while(t < j):
        x = random.randint(0, i)
        y = random.randint(0, i)
        if not (x, y) in L and x != y:
            # print("adding")
            # print(x)
            # print(y)
            G.add_edge(x, y)
            L.append((x, y))
            t += 1
    return G



# PART 1
#--------------------------- EXPERIMENT 1 ---------------------------
# edges = []
# for i in range(1, 250, 5) :
#     edges.append(i)
# def exp1(list_of_edges, num_of_graphs) :
#     num_of_cycles = 0
#     cycles_per_edge = []
#     for edge in list_of_edges :
#         for i in range(num_of_graphs) :
#             G = create_random_graph(100, edge)
#             if has_cycle(G) :
#                 num_of_cycles += 1
#         cycles_per_edge.append(num_of_cycles / num_of_graphs)
#         num_of_cycles = 0
#     return (list_of_edges, cycles_per_edge)


# test = exp1(edges, 100)
# plot.xlabel("Number of Edges")
# plot.ylabel("Probability of Cycle Occurring")
# plot.plot(test[0], test[1])
# # legend = plot.legend(loc="upper center")
# plot.title("Probabilty of Cycles Occurring in Graphs with Different Numbers of Edges")
# plot.show()
    
#--------------------------- EXPERIMENT 2 ------------------------------

#def experimentTwo(f, E, times):
#    L = []
#    z = 0
#    for edge in E:
#        for x in range(0, times):
#            exp2Graph = create_random_graph(f, edge)
#            if is_connected(exp2Graph):
#                z += 1
#        L.append(z/times)
#        z = 0
#    return L

#fixedNumberOfNodes = 100
#numberOfEdges = [10, 50, 100, 150, 200, 300, 400]
#expirmentTwoTest = experimentTwo(fixedNumberOfNodes, numberOfEdges, 10)
#plot.xlabel("Number of Edges")
#plot.ylabel("Probability Of Connected Graphs")
#plot.plot(numberOfEdges, expirmentTwoTest)
#plot.title("Probability of Graph Being Connected with Different Number of Edges")
#plot.show()

# PART 2

#----------------- Approximation experiment 1  -----------------
# (edges are the independent var, num of nodes kept constant)

# edges1 = [1, 5, 10, 15, 20, 25, 30,]
# def pt2exp1(list_of_edges, num_of_graphs) :
#     MVC_sum = 0
#     MVC_sum_per_edge = []
#     approx1_sum = 0
#     approx1_sum_per_edge = []
#     approx2_sum = 0
#     approx2_sum_per_edge = []
#     approx3_sum = 0
#     approx3_sum_per_edge = []
#     for edge in list_of_edges :
#         for i in range(num_of_graphs) :
#             G = create_random_graph(8, edge)
#             MVC_sum += len(MVC(G))
#             approx1_sum += len(approx1(G))
#             approx2_sum += len(approx2(G))
#             approx3_sum += len(approx3(G))
#         MVC_sum_per_edge.append(MVC_sum)
#         approx1_sum_per_edge.append(approx1_sum)
#         approx2_sum_per_edge.append(approx2_sum)
#         approx3_sum_per_edge.append(approx3_sum)
#         MVC_sum = 0
#         approx1_sum = 0
#         approx2_sum = 0
#         approx3_sum = 0
#     return (list_of_edges, MVC_sum_per_edge, approx1_sum_per_edge, approx2_sum_per_edge, approx3_sum_per_edge)


# test1 = pt2exp1(edges1, 1000)
# plot.xlabel("Number of edges")
# plot.ylabel("Sum of the sizes of Vertex Covers for 1000 graphs")
# plot.plot(test1[0], test1[1], label="MVC Sum")
# plot.plot(test1[0], test1[2], label="approx1 Sum")
# plot.plot(test1[0], test1[3], label="approx2 Sum")
# plot.plot(test1[0], test1[4], label="approx3 Sum")
# legend = plot.legend(loc="upper left")
# plot.title("Sum of Sizes of Vertex Covers Depending on the Number of Edges")
# plot.show()
    
#----------------- Approximation experiment 2  -----------------
# (nodes are the independent var, num of edges kept constant)
# nodes = [5, 8, 15,]
# def pt2exp2(list_of_nodes, num_of_graphs) :
#     MVC_sum = 0
#     MVC_sum_per_edge = []
#     approx1_sum = 0
#     approx1_sum_per_edge = []
#     approx2_sum = 0
#     approx2_sum_per_edge = []
#     approx3_sum = 0
#     approx3_sum_per_edge = []
#     for node in list_of_nodes :
#         for i in range(num_of_graphs) :
#             G = create_random_graph(node, 10)
#             MVC_sum += len(MVC(G))
#             approx1_sum += len(approx1(G))
#             approx2_sum += len(approx2(G))
#             approx3_sum += len(approx3(G))
#         MVC_sum_per_edge.append(MVC_sum)
#         approx1_sum_per_edge.append(approx1_sum)
#         approx2_sum_per_edge.append(approx2_sum)
#         approx3_sum_per_edge.append(approx3_sum)
#         MVC_sum = 0
#         approx1_sum = 0
#         approx2_sum = 0
#         approx3_sum = 0
#     return (list_of_nodes, MVC_sum_per_edge, approx1_sum_per_edge, approx2_sum_per_edge, approx3_sum_per_edge)

# test2 = pt2exp2(nodes, 500)
# plot.xlabel("Number of nodes")
# plot.ylabel("Sum of the sizes of Vertex Covers for 100 graphs")
# plot.plot(test2[0], test2[1], label="MVC Sum")
# plot.plot(test2[0], test2[2], label="approx1 Sum")
# plot.plot(test2[0], test2[3], label="approx2 Sum")
# plot.plot(test2[0], test2[4], label="approx3 Sum")
# legend = plot.legend(loc="upper left")
# plot.title("Sum of Sizes of Vertex Covers Depending on the Number of Nodes")
# plot.show()

#----------------- Approximation experiment 3  -----------------
#(edges are the independent var, num of nodes kept constant)
# def pt2exp3() :
#     G = Graph(7)
#     graph_num = []
#     graphs_generated = 0
#     count = 0
#     nodes = []
#     for i in G.adj :
#         nodes.append(i)
    
#     edges = combinations(nodes, 2)

#     MVC_sum = 0
#     MVC_sum_per_edge = []
#     approx1_sum = 0
#     approx1_sum_per_edge = []
#     approx2_sum = 0
#     approx2_sum_per_edge = []
#     approx3_sum = 0
#     approx3_sum_per_edge = []

#     #graphs with no edges
#     MVC_sum += len(MVC(G))
#     approx1_sum += len(approx1(G))
#     approx2_sum += len(approx2(G))
#     approx3_sum += len(approx3(G))
#     MVC_sum_per_edge.append(MVC_sum)
#     approx1_sum_per_edge.append(approx1_sum)
#     approx2_sum_per_edge.append(approx2_sum)
#     approx3_sum_per_edge.append(approx3_sum)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     count += 1
#     graph_num.append(count)
    
#     #graphs with one edge
#     for i in edges :
#         G.add_edge(i[0], i[1])
#         MVC_sum += len(MVC(G))
#         approx1_sum += len(approx1(G))
#         approx2_sum += len(approx2(G))
#         approx3_sum += len(approx3(G))
#         graphs_generated += 1
#         # print("one edge: " +str(graphs_generated))
#     count += 1
#     graph_num.append(count)
#     MVC_sum_per_edge.append(MVC_sum/graphs_generated)
#     approx1_sum_per_edge.append(approx1_sum/graphs_generated)
#     approx2_sum_per_edge.append(approx2_sum/graphs_generated)
#     approx3_sum_per_edge.append(approx3_sum/graphs_generated)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     graphs_generated = 0

#     #graphs with two edges
#     edges = combinations(nodes, 2)
#     edge_pairs = combinations(edges, 2)
#     for i in edge_pairs :
#         G.add_edge(i[0][0], i[0][1])
#         G.add_edge(i[1][0], i[1][1])
#         MVC_sum += len(MVC(G))
#         approx1_sum += len(approx1(G))
#         approx2_sum += len(approx2(G))
#         approx3_sum += len(approx3(G))
#         graphs_generated += 1
#         # print("two edge: " +str(graphs_generated))
#     count += 1
#     graph_num.append(count)
#     MVC_sum_per_edge.append(MVC_sum/graphs_generated)
#     approx1_sum_per_edge.append(approx1_sum/graphs_generated)
#     approx2_sum_per_edge.append(approx2_sum/graphs_generated)
#     approx3_sum_per_edge.append(approx3_sum/graphs_generated)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     graphs_generated = 0

#     edges = combinations(nodes, 2)
#     edge_triples = combinations(edges, 3)
#     #graphs with 3 edges
#     for i in edge_triples :
#         G.add_edge(i[0][0], i[0][1])
#         G.add_edge(i[1][0], i[1][1])
#         G.add_edge(i[2][0], i[2][1])
#         MVC_sum += len(MVC(G))
#         approx1_sum += len(approx1(G))
#         approx2_sum += len(approx2(G))
#         approx3_sum += len(approx3(G))
#         graphs_generated += 1
#     count += 1
#     graph_num.append(count)
#     MVC_sum_per_edge.append(MVC_sum/graphs_generated)
#     approx1_sum_per_edge.append(approx1_sum/graphs_generated)
#     approx2_sum_per_edge.append(approx2_sum/graphs_generated)
#     approx3_sum_per_edge.append(approx3_sum/graphs_generated)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     graphs_generated = 0

#     #graphs with 4 edges
#     edges = combinations(nodes, 2)
#     edge_quads = combinations(edges, 4)
#     for i in edge_quads :
#         G.add_edge(i[0][0], i[0][1])
#         G.add_edge(i[1][0], i[1][1])
#         G.add_edge(i[2][0], i[2][1])
#         G.add_edge(i[3][0], i[3][1])
#         MVC_sum += len(MVC(G))
#         approx1_sum += len(approx1(G))
#         approx2_sum += len(approx2(G))
#         approx3_sum += len(approx3(G))
#         graphs_generated += 1
#     count += 1
#     graph_num.append(count)
#     MVC_sum_per_edge.append(MVC_sum/graphs_generated)
#     approx1_sum_per_edge.append(approx1_sum/graphs_generated)
#     approx2_sum_per_edge.append(approx2_sum/graphs_generated)
#     approx3_sum_per_edge.append(approx3_sum/graphs_generated)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     graphs_generated = 0

#     #graphs with 5 edges
#     edges = combinations(nodes, 2)
#     edge_quads = combinations(edges, 5)
#     for i in edge_quads :
#         G.add_edge(i[0][0], i[0][1])
#         G.add_edge(i[1][0], i[1][1])
#         G.add_edge(i[2][0], i[2][1])
#         G.add_edge(i[3][0], i[3][1])
#         G.add_edge(i[4][0], i[4][1])
#         MVC_sum += len(MVC(G))
#         approx1_sum += len(approx1(G))
#         approx2_sum += len(approx2(G))
#         approx3_sum += len(approx3(G))
#         graphs_generated += 1
#     count += 1
#     graph_num.append(count)
#     MVC_sum_per_edge.append(MVC_sum/graphs_generated)
#     approx1_sum_per_edge.append(approx1_sum/graphs_generated)
#     approx2_sum_per_edge.append(approx2_sum/graphs_generated)
#     approx3_sum_per_edge.append(approx3_sum/graphs_generated)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     graphs_generated = 0

#     #graphs with 6 edges 
#     edges = combinations(nodes, 2)
#     edge_quads = combinations(edges, 6)
#     for i in edge_quads :
#         G.add_edge(i[0][0], i[0][1])
#         G.add_edge(i[1][0], i[1][1])
#         G.add_edge(i[2][0], i[2][1])
#         G.add_edge(i[3][0], i[3][1])
#         G.add_edge(i[4][0], i[4][1])
#         G.add_edge(i[5][0], i[5][1])
#         MVC_sum += len(MVC(G))
#         approx1_sum += len(approx1(G))
#         approx2_sum += len(approx2(G))
#         approx3_sum += len(approx3(G))
#         graphs_generated += 1
#     count += 1
#     graph_num.append(count)
#     MVC_sum_per_edge.append(MVC_sum/graphs_generated)
#     approx1_sum_per_edge.append(approx1_sum/graphs_generated)
#     approx2_sum_per_edge.append(approx2_sum/graphs_generated)
#     approx3_sum_per_edge.append(approx3_sum/graphs_generated)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     graphs_generated = 0

#     #graphs with 7 edges 
#     edges = combinations(nodes, 2)
#     edge_quads = combinations(edges, 7)
#     for i in edge_quads :
#         G.add_edge(i[0][0], i[0][1])
#         G.add_edge(i[1][0], i[1][1])
#         G.add_edge(i[2][0], i[2][1])
#         G.add_edge(i[3][0], i[3][1])
#         G.add_edge(i[4][0], i[4][1])
#         G.add_edge(i[5][0], i[5][1])
#         G.add_edge(i[6][0], i[6][1])
#         MVC_sum += len(MVC(G))
#         approx1_sum += len(approx1(G))
#         approx2_sum += len(approx2(G))
#         approx3_sum += len(approx3(G))
#         graphs_generated += 1
#     count += 1
#     graph_num.append(count)
#     MVC_sum_per_edge.append(MVC_sum/graphs_generated)
#     approx1_sum_per_edge.append(approx1_sum/graphs_generated)
#     approx2_sum_per_edge.append(approx2_sum/graphs_generated)
#     approx3_sum_per_edge.append(approx3_sum/graphs_generated)
#     MVC_sum = 0
#     approx1_sum = 0
#     approx2_sum = 0
#     approx3_sum = 0
#     graphs_generated = 0

#     return (graph_num, MVC_sum_per_edge, approx1_sum_per_edge, approx2_sum_per_edge, approx3_sum_per_edge)

# test3 = pt2exp3()
# plot.xlabel("Number of Edges")
# plot.ylabel("Sum of the Sizes of Vertex Covers Divided by number of Graphs Generated")
# plot.plot(test3[0], test3[4], label="Average approx3 Sum")
# plot.plot(test3[0], test3[3], label="Average approx2 Sum")
# plot.plot(test3[0], test3[2], label="Average approx1 Sum")
# plot.plot(test3[0], test3[1], label="Average MVC Sum")
# legend = plot.legend(loc="upper left")
# plot.title("Sum of Sizes of Vertex Covers for all possible graphs of size 7")
# plot.show()

#============== CODE FOR THE INDEPENDENT SET PROBLEM ===================

# code for finding Max Indep Set
def MIS(G):
    void = []
    L = []
    for x in range(0, G.number_of_nodes()): #grab a vertex x
        for z in range(0, G.number_of_nodes()): #grab all vertex s.t x is not adjacent to those
            if not (z in G.adj[x]):
                L.append(z)
        while(connectionsExists(G, L)): #while there exists a vertex in list that contains an edge to another vertex in the list
            max = L[0]
            for elm in L: #find the vertex with the max amount of conflicting edges and remove it
                if (amountConnected(G, elm, L) > amountConnected(G, max, L)): max = elm
            L.remove(max)
        L = []
        void.append(L) #store list and repeat on next vertex
    top = []
    #print(void)
    for y in void:
        if len(y) > len(top): top = y
    return top #return the largets MIS found
    
# helper function for MIS
def amountConnected(G, v, L):
    counter = 0
    for x in G.adj[v]:
        if x in L: counter += 1
    return counter

# helper function for MIS
def connectionsExists(G, L):
    for z in L: #for each vertex
        for q in L: #for each vertex
            if (q in G.adj[z]): #check if any vertex in the list has q adjacent to it
                return True
    return False

# Finding out relationship with MIS and MVCs
def MIS_MVC_test(n):
    G = create_random_graph(n - 1, n//2)
    print("Graph with " + str(n) + " nodes and the " + str(n//2) + " edges with a adjacency dictionary of ")
    print(G.adj)
    print("")
    print("Has a MVC of " + str(MVC(G)) + " and has a MIS of " + str(MIS(G)))
    print("When you sum the size of both lists you get: " + str(len(MVC(G) + MIS(G))))
    return

# Testing MIS and MVC relationship
#MIS_MVC_test(6)
#MIS_MVC_test(7)
#MIS_MVC_test(8)
#MIS_MVC_test(9)
#MIS_MVC_test(10)

