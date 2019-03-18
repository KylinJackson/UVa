import sys
import copy

n = int(input())
x = list()


class Pile:
    def __init__(self, bottom):
        self.bottom = bottom
        self.above = [bottom]

    def add(self, block):
        self.above.append(block)

    def remove(self, block):
        self.above.remove(block)

    def exist(self, block):
        return block in self.above

    def setback(self, block):
        flag = False
        pile_tmp = copy.deepcopy(self.above)
        for block_tmp in pile_tmp:
            if flag:
                x[block_tmp].add(block_tmp)
                self.remove(block_tmp)
            if block_tmp == block:
                flag = True

    def __str__(self):
        print_str = str(self.bottom) + ':'
        if len(self.above) != 0:
            print_str += ' ' + ' '.join(map(str, self.above))
        return print_str


class Order:
    def __init__(self, command_str):
        command = command_str.split()
        self.op1 = command[0]
        self.op2 = command[2]
        self.block1 = int(command[1])
        self.block2 = int(command[3])
        # find where block1 and block2 located
        for bottom, pile in enumerate(x):
            if pile.exist(self.block1):
                self.block1_bottom = bottom
                break
        for bottom, pile in enumerate(x):
            if pile.exist(self.block2):
                self.block2_bottom = bottom
                break

    def move(self):
        flag = False
        pile_tmp = copy.deepcopy(x[self.block1_bottom])
        for block1_tmp in pile_tmp.above:
            if block1_tmp == self.block1 or flag:
                flag = True
                x[self.block2_bottom].add(block1_tmp)
                x[self.block1_bottom].remove(block1_tmp)

    def check(self):
        return self.block1 != self.block2 \
               and self.block1_bottom != self.block2_bottom


for i in range(n):
    x.append(Pile(i))

for line in sys.stdin:
    if line == "quit\n":
        for v in x:
            print(v)
        break
    order = Order(line)
    if order.check():
        if order.op1 == "move" and order.op2 == "onto":
            x[order.block1_bottom].setback(order.block1)
            x[order.block2_bottom].setback(order.block2)
            x[order.block2_bottom].add(order.block1)
            x[order.block1_bottom].remove(order.block1)
        if order.op1 == "move" and order.op2 == "over":
            x[order.block1_bottom].setback(order.block1)
            x[order.block2_bottom].add(order.block1)
            x[order.block1_bottom].remove(order.block1)
        if order.op1 == "pile" and order.op2 == "onto":
            x[order.block2_bottom].setback(order.block2)
            order.move()
        if order.op1 == "pile" and order.op2 == "over":
            order.move()
