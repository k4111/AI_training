class Node:
    def __init__(self, ID, prev_node=None, h=0):
        self.ID = ID
        self.prev_node = prev_node
        self.h = h


def get_path(node, path, weight):
    path.insert(0, node.ID)
    weight += node.h
    if node.prev_node == None:
        print(path)
        print('cost: {0}'.format(weight))
        return
    else:
        get_path(node.prev_node, path, weight)


def duplicate(list, node):
    for element in list:
        if node.ID == element.ID and node.h == element.h:
            return True
    return False


def best_first_search(input_graph, start, stop):
    start_node = Node(ID=start, h=input_graph[start][-1])
    stop_node = Node(ID=stop)
    pending = []
    checked = []
    pending.insert(0, start_node)
    while len(pending) != 0:
        current_node = pending.pop(0)
        if current_node.ID == stop_node.ID:
            path = []
            weight = 0
            print('search successful')
            get_path(current_node, path, weight)
            return
        checked.insert(0, current_node)
        neighbourhood = input_graph[current_node.ID]
        for i in range(0, len(neighbourhood)-1):
            neighbour_ID = neighbourhood[i]
            neighbour_h = input_graph[neighbour_ID][-1]
            neighbour = Node(ID=neighbour_ID, prev_node=current_node, h=neighbour_h)
            if (not duplicate(pending, neighbour)) and (not duplicate(checked, neighbour)):
                pending.insert(0, neighbour)
        pending.sort(key=lambda node: node.h)
        '''
        print(list(map(lambda node: '{0} - {1}'.format(node.ID, node.h), pending)))
        print(list(map(lambda node: '{0} - {1}'.format(node.ID, node.h), checked)))
        print('---')
        '''
    print('search failed')
    return


graph = {
    'A': ['C', 'D', 'E', 20],
    'B': ['F', 'I', 'G', 'H', 0],
    'C': ['A', 'F', 15],
    'D': ['A', 'F', 'I', 6],
    'E': ['A', 'K', 'G', 7],
    'F': ['B', 'C', 'D', 10],
    'G': ['E', 'I', 'H', 'B', 5],
    'H': ['B', 'G', 3],
    'I': ['D', 'B', 'G', 8],
    'K': ['E', 12],
}

best_first_search(graph, 'A', 'B')