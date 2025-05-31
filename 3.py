import networkx as nx
number_of_nodes = 30
random_edge_percent = 0.75
G = nx.erdos_renyi_graph(number_of_nodes, random_edge_percent)
a = 0
for n in G.nodes():
    a = a + G.degree(n)
print(f"Средняя степень вершины, вычисляемая встроенной функцией {float(a) / len(G.nodes())}")
print(f"Cредняя степень вершины по формуле из лекции {(30 - 1) * 0.75}")
