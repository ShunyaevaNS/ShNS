import networkx as nx
number_of_nodes = 30
random_edge_percent = 0.75
G = nx.erdos_renyi_graph(number_of_nodes, random_edge_percent)
a = 0
for n in G.nodes():
    a = a + G.degree(n)
print(f'Cредняя степень вершины: {float(a) / len(G.nodes())}')
print(
    f'Cредняя степень вершины по представленной формуле: '
    f'{(number_of_nodes - 1) * random_edge_percent}')
