from math import pi

class SquareIntoCircle:
    def __init__(self, side):
        self.side = side
    
    def size(self):
        radius = self.side / 2
        return round(radius, 3)
    
    def area(self):
        radius = self.side / 2
        area = pi * (radius ** 2)
        return round(area, 3)


class CircleIntoSquare:
    def __init__(self, radius):
        self.radius = radius
    
    def size(self):
        side = 2 * self.radius
        return round(side, 3)
    
    def area(self):
        side = 2 * self.radius
        area = side ** 2
        return round(area, 3)




sq = SquareIntoCircle(1)
print(sq.size(), sq.area(), sep='\n')  # 0.637, 1.273
print()
circle = CircleIntoSquare(sq.size())
print(circle.size(), circle.area(), sep='\n')  # 1.001, 1.001