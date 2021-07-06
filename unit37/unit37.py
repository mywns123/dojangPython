import math


class Point2D:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def PointPrint(self):
        print("p : {}, {}".format(self.__x, self.__y))

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__x = y

    def setXY(self, x, y):
        self.x = x
        self.x = y


p1 = Point2D(10, 20)
p2 = Point2D(100, 200)

# p1.PointPrint()
# p2.PointPrint()


class LineDraw:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


# li = LineDraw(p1, p2)
# li.p1.PointPrint()


a = p2.getX() - p1.getX()
b = p2.getY() - p1.getY()
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
d = math.sqrt(a**2 + b**2)

print(c)
print(d)

