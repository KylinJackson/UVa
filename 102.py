import sys

for line in sys.stdin:
    bottles = [int(x) for x in line.split()]
    bottle_num = sum(bottles)
    left = list()
    left.append(bottles[0] + bottles[4] + bottles[8])  # BGC
    left.append(bottles[0] + bottles[5] + bottles[7])  # BCG
    left.append(bottles[1] + bottles[3] + bottles[8])  # GBC
    left.append(bottles[1] + bottles[5] + bottles[6])  # GCB
    left.append(bottles[2] + bottles[3] + bottles[7])  # CBG
    left.append(bottles[2] + bottles[4] + bottles[6])  # CGB

    left_max = max(left)
    if left[1] == left_max:
        print("BCG", bottle_num - left_max)
    elif left[0] == left_max:
        print("BGC", bottle_num - left_max)
    elif left[4] == left_max:
        print("CBG", bottle_num - left_max)
    elif left[5] == left_max:
        print("CGB", bottle_num - left_max)
    elif left[2] == left_max:
        print("GBC", bottle_num - left_max)
    elif left[3] == left_max:
        print("GCB", bottle_num - left_max)
