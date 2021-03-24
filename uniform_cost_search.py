class Node:
    def __init__(self, ID, prev_node=None, g=0):
        self.ID = ID
        self.prev_node = prev_node
        self.g = g


def get_path(node, path):
    path.insert(0, node.ID)
    if node.prev_node == None:
        return
    else:
        get_path(node.prev_node, path)


def duplicate(list, node):
    for element in list:
        if node.ID == element.ID and node.g > element.g:
            return True
    return False


def uniform_cost_search(input_graph, start, stop):
    start_node = Node(ID=start)
    stop_node = Node(ID=stop)
    pending = []
    checked = []
    pending.insert(0, start_node)
    while len(pending) != 0:
        current_node = pending.pop(0)
        if current_node.ID == stop_node.ID:
            path = []
            get_path(current_node, path)
            print('search successful')
            print(path)
            print('cost: {0}'.format(current_node.g))
            return
        checked.insert(0, current_node)
        neighbourhood = input_graph[current_node.ID]
        for i in range(0, len(neighbourhood), 2):
            neighbour_ID = neighbourhood[i]
            neighbour_g = neighbourhood[i+1] + current_node.g
            neighbour = Node(ID=neighbour_ID, prev_node=current_node, g=neighbour_g)
            if (not duplicate(pending, neighbour)) and (not duplicate(checked, neighbour)):
                pending.insert(0, neighbour)
        pending.sort(key=lambda node: node.g)
        '''
        print(list(map(lambda node: '{0} - {1}'.format(node.ID, node.g), pending)))
        print(list(map(lambda node: '{0} - {1}'.format(node.ID, node.g), checked)))
        print('---')
        '''
    print('search failed')
    return


graph = {
    'A': ['B', 5, 'D', 3],
    'B': ['A', 5, 'C', 1, 'E', 4],
    'C': ['B', 1, 'E', 6, 'G', 8],
    'D': ['A', 3, 'E', 2, 'F', 2],
    'E': ['B', 4, 'C', 6, 'D', 2, 'G', 4],
    'F': ['D', 2, 'G', 3],
    'G': ['C', 8, 'E', 4, 'F', 3]
}
uniform_cost_search(graph, 'B', 'F')