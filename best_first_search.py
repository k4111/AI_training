graph = {
    'A': ['B', 'C', 'D', 6],
    'B': ['E', 'F', 3],
    'C': ['G', 'H', 4],
    'D': ['I', 'J', 5],
    'E': [3],
    'F': ['K', 'L', 'M', 1],
    'G': [6],
    'H': ['N', 'O', 2],
    'I': [5],
    'J': [4],
    'K': [2],
    'L': [0],
    'M': [4],
    'N': [0],
    'O': [4]
}

class Node:
    def __init__(self, id, par=None, h=0):
        self.id = id
        self.par = par
        self.h = h

def get_path(node, distance):
    print(node.id)
    distance += node.h
    if node.par == None:
        print(distance)
        return
    else:
        get_path(node.par, distance)

def get_distance(node):
    return node.h

def best_first_search(start_node, end_node, graph):
    wait_to_check = []
    checked = []
    wait_to_check.insert(0, start_node)
    start_node.h = graph[start_node.id][-1]
    while len(wait_to_check) != 0:
        node = wait_to_check.pop(0)
        checked.append(node)
        if node.id == end_node.id:
            print('search successfully')
            distance = 0
            get_path(node, distance)
            return
        i = 0
        while i < len(graph[node.id]) - 1:
            id = graph[node.id][i]
            h = graph[id][-1]
            tmp = Node(id=id, par=node, h=h)
            if (tmp not in wait_to_check) and (tmp not in checked):
                wait_to_check.insert(0, tmp)
            i += 1
        wait_to_check.sort(key=get_distance)
    print('search failed')
    return

best_first_search(Node(id='A'), Node(id='N'), graph)


