class Ship:

    def __init__(self, length, horizontal):
        self.length = length
        self.horizontal = horizontal
        self.x = -1
        self.y = -1
        self.hitmap = [0] * length
        self.hits = 0

    def inside(self, x, y):
        if self.horizontal and y == self.y and x >= self.x and x <= self.x + self.length:
            return True
        if not self.horizontal and x == self.x and y >= self.y and y <= self.y + self.length:
            return True
        return False

    def checkHit(self, x, y):
        index = -1
        if not self.horizontal:
            index = y - self.y - 1
        else:
            index = x - self.x - 1
        if (self.hitmap[index] == 0):
            self.hits += 1
            self.hitmap[index] = 1
            return True
        return False

    def __eq__(self, other):
        if self.horizontal:
            if other.horizontal:
                if self.y == other.y:
                    if (self.x + self.length > other.x) or (other.x + other.length > self.x):
                        return True
            else:
                if (self.y >= other.y and self.y <= other.y + other.length) and (
                        other.x >= self.x and other.x <= self.x + self.length):
                    return True
        else:
            if not other.horizontal:
                if self.x == other.x:
                    if (self.y + self.length > other.y) or (other.y + other.length > self.y):
                        return True
            else:
                if (other.y >= self.y and other.y <= self.y + self.length) and (
                        self.x >= other.x and self.x <= other.x + other.length):
                    return True
        return False

    def __str__(self):
        return str(self.x) + " " + str(self.y)




