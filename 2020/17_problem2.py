import pdb
class Node:
    def __init__(self, point, state):
        self.point = point
        self.neighbors = set()
        self.state = state
        self.new_state = state

    def get_neighbor_coordinates(self):
        coordinates = []
        for w in range(-1,2):
            for z in range(-1,2):
                for y in range(-1,2):
                    for x in range(-1,2):
                        neighbor_point = tuple([a+b for a,b in zip(self.point, (x,y,z,w))])
                        if neighbor_point != self.point:
                            coordinates.append(neighbor_point)
        return coordinates

    def update_neighbors(self, nodes):
        self.neighbors = set()
        for neighbor_point in self.get_neighbor_coordinates():
            neighbor = nodes.get(neighbor_point, None)
            if neighbor:
                neighbor.neighbors.add(self)
                self.neighbors.add(neighbor)

    def add_inactive_neighbors(self, nodes):
        for neighbor_point in self.get_neighbor_coordinates():
            if neighbor_point in nodes:
                continue
            nodes[neighbor_point] = Node(neighbor_point, False)
        self.update_neighbors(nodes)

    def count_neighbors(self, state):
        return len([node for node in self.neighbors if node.state == state])

    def apply_rules(self, nodes):
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
        # Otherwise, the cube becomes inactive.
        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
        # Otherwise, the cube remains inactive.
        active_neighbors = self.count_neighbors(state=True)
        if self.state == True and active_neighbors not in [2,3]:
            self.new_state = False
        elif self.state == False and active_neighbors == 3:
            self.new_state = True

    def commit_state(self):
        self.state = self.new_state

nodes = {}

def get_board(filename):
    with open(filename, 'r') as f:
        rows = f.read().split('\n')
        height = len(rows)
        width = len(rows[0])
        grid = [cell for row in rows for cell in row]
        z,w = 0,0
        for y in range(height):
            for x in range(width):
                if grid[y*width+x] == '#':
                    nodes[(x,y,z,w)] = Node((x,y,z,w), True)
    return nodes

def update_neighbors(nodes):
    for node in nodes.values():
        node.update_neighbors(nodes)

def iterate(nodes):
    # add inactive neighbors to all active nodes
    for node in nodes.values():
        node.add_inactive_neighbors(nodes)
    # iterate through nodes, apply rules to new_state
    for node in nodes.values():
        node.apply_rules(nodes)
    # commit new_state to state
    for node in nodes.values():
        node.commit_state()
    # remove all inactive nodes (?)

def count_active_nodes(nodes):
    return len([node for node in nodes.values() if node.state == True])

def problem_1(nodes):
    # How many cubes are left in the active state after the sixth cycle?

    for _ in range(6):
        iterate(nodes)

    # count cubes
    return count_active_nodes(nodes)


# filename = '17_test.txt'
filename = '17_input.txt'
nodes = get_board(filename)
update_neighbors(nodes)


result = problem_1(nodes)
print(result)

