import sys


class Box:
    def __init__(self, dim, coordinate):
        self.dim = dim
        self.coordinate = coordinate.sort()
        self.next_box = []

    def next_array(self):
        result = []
        for index in range(self.dim):
            if index in self.next_box:
                result.append(2)
            else:
                result.append(1)
        return result

    def add_next(self, next_box):
        self.next_box.append(next_box)

    def __eq__(self, other):
        for index in range(self.dim):
            if self.coordinate[index] != other.coordinate[index]:
                return False
        return True

    def __lt__(self, other):
        for index in range(self.dim):
            if self.coordinate[index] >= other.coordinate[index]:
                return False
        return True

    def __gt__(self, other):
        for index in range(self.dim):
            if self.coordinate[index] <= other.coordinate[index]:
                return False
        return True

    def __ge__(self, other):
        for index in range(self.dim):
            if self.coordinate[index] < other.coordinate[index]:
                return False
        return True

    def __le__(self, other):
        for index in range(self.dim):
            if self.coordinate[index] > other.coordinate[index]:
                return False
        return True


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dim = len(matrix)

    def get_longest_path(self):
        for start in range(self.dim):
            pass


def find_next(boxes):
    for box1 in boxes:
        for key, box2 in enumerate(boxes):
            if box1 is box2:
                continue
            if box1 < box2:
                box1.add_next(key)


def setup_chain(boxes):
    box_next_matrix = []
    for box in boxes:
        box_next_matrix.append(box.next_array())
    graph = Graph(box_next_matrix)
    return graph.get_longest_path()


box_list = []
for line in sys.stdin:
    k, n = map(int, line.split())
    for i in range(k):
        box_list.append(Box(n, list(map(int, input().split()))))
    setup_chain(box_list)
