import math


def find_distance(x1, x2, y1, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return distance

print("Find distance")
print(find_distance(7, 3, 15, 10))
