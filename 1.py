import sys
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.make_graph(nodes, init_graph)
    def make_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for neighbour_node, value in edges.items():
                if graph[neighbour_node].get(node, False) is False:
                    graph[neighbour_node][node] = value
        return graph
    def get_nodes(self):
        return self.nodes
    def get_outbound_edges(self, node):
        relationship = []
        for outbound_node in self.nodes:
            if self.graph[node].get(outbound_node, False) is not False:
                relationship.append(outbound_node)
        return relationship
    def value(self, node1, node2):
        return self.graph[node1][node2]
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    s_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        s_path[node] = max_value
    s_path[start_node] = 0
    while unvisited_nodes:
        cur_min_node = None
        for node in unvisited_nodes:
            if cur_min_node is None:
                cur_min_node = node
            elif s_path[node] < s_path[cur_min_node]:
                cur_min_node = node
        neighbors = graph.get_outbound_edges(cur_min_node)
        for n in neighbors:
            temp_value = s_path[cur_min_node] + graph.value(cur_min_node, n)
            if temp_value < s_path[n]:
                s_path[n] = temp_value
                previous_nodes[n] = cur_min_node
        unvisited_nodes.remove(cur_min_node)
    return previous_nodes, s_path
def print_result(previous_nodes, s_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)
    print(
        f'Наиболее короткий путь - {start_node} - {target_node}:',
        ' -> '.join([str(item) for item in reversed(path)])
    )
    print(f'Итого: {s_path[target_node]}')
if __name__ == '__main__':
    '''
    '''
    nodes = [1, 2, 3, 4, 5, 6]
    init_graph = {
        1: {2: 7, 3: 9, 6: 14}, 
        2: {4: 15, 3: 10, 1: 7}, 
        3: {4: 11, 6: 2, 1: 9, 2: 10}, 
        4: {5: 6, 3: 11, 2: 15},
        5: {6: 9, 4: 6},
        6: {1: 14, 3: 2, 5: 9}
    }
    graph = Graph(nodes, init_graph)
    start_node = 1
    previous_nodes, s_path = dijkstra_algorithm(
        graph=graph, start_node=start_node
        )
    for node in nodes:
        if node != start_node:
            print_result(
                previous_nodes,
                s_path,
                start_node=start_node,
                target_node=node
            )