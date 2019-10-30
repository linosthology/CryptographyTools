# on input
# p, a, b, P, Q
#
# process
# find all Elements to get the order
#

import extendedEuclidian
import sys
args = sys.argv[1:]


def turnPositive(mod, element):
    if element < 0:
        return mod + element
    else:
        return element


class ellipticCurve:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b
        self.calculateOrder()

    def calculateOrder(self):
        self.points = []
        possibleYs = []
        # get all possible y values
        for x in range(0, self.p, 1):
            possibleYs.append((x*x) % self.p)
        # check if y values exist for current x
        for x in range(0, self.p, 1):
            fX = (x ** 3 + self.a * x + self.b) % self.p
            for i in range(len(possibleYs)):
                if possibleYs[i] == fX:
                    y = i
                    self.points.append((x, y))
        self.order = len(self.points)

    def getInfo(self):
        print(
            f"\nthe given elliptic curve has these points:\n{self.points}\nand an order of {len(self.points)}")


class pointAddition:
    def __init__(self, P, Q):
        self.P = P
        self.Q = Q
    gradient: int

    def calculate(self):
        if self.P == self.Q:
            print(
                "you can't do addition with the same point, you need to perform point duplication")
        else:
            divident = self.Q[1]-self.P[1] % curve.p
            diviser = self.Q[0]-self.P[0] % curve.p
            inverse = extendedEuclidian.getInverse(curve.p, diviser)
            gradient = divident*inverse % curve.p
        x = (gradient ** 2 - self.P[0] - self.Q[0]) % curve.p
        y = turnPositive(
            curve.p, ((gradient*(self.P[0]-x)-self.P[1]) % curve.p))
        print(f"\n{self.P} + {self.Q} is ({x}, {y})!")


class pointDuplication:
    def __init__(self, P):
        self.P = P
    gradient: int

    def calculate(self):
        divident = (3*(self.P[0]**2) + curve.a) % curve.p
        diviser = 2 * self.P[1] % curve.p
        inverse = extendedEuclidian.getInverse(curve.p, diviser)
        gradient = divident*inverse % curve.p
        x = (gradient ** 2 - self.P[0] - self.P[0]) % curve.p
        y = turnPositive(
            curve.p, ((gradient*(self.P[0]-x)-self.P[1]) % curve.p))
        print(f"\n{self.P} + {self.P} is ({x}, {y})!")


def pointExists(x, y):
    givenPoint = (x, y)
    isPoint = False
    for point in curve.points:
        if givenPoint == point:
            isPoint = True
    return isPoint


if 3 <= len(args) <= 7:
    try:
        curve = ellipticCurve(int(args[0]), int(args[1]), int(args[2]))
        curve.getInfo()
        if len(args) == 4:
            print("\na point needs a x and a y value")
        elif len(args) == 5:
            x = int(args[3])
            y = int(args[4])
            if pointExists(x, y):
                duplication = pointDuplication((x, y))
                duplication.calculate()
            else:
                print("the given point is not an element of the group")
        elif len(args) == 6:
            print("\na point needs a x and a y value")
        elif len(args) == 7:
            x1 = int(args[3])
            y1 = int(args[4])
            x2 = int(args[5])
            y2 = int(args[6])
            if pointExists(x1, y1) and pointExists(x2, y2):
                addition = pointAddition((x1, y1), (x2, y2))
                addition.calculate()
            else:
                print("one of the given points is not an element of the group")

    except:
        print("\nthe arguments need to be integers! try again...")

else:
    print("\nyou need to enter a modulus and both a and b for the curve\nhere is an example\npy ellipticCurveGroupOperations.py p a b")
    print("\nyou can also enter two or four more arguments to perform point duplication or addition with them")
