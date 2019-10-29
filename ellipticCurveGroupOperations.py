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
    def __init__(self, P: (int, int), Q: (int, int)):
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


if len(args) == 3:
    try:
        curve = ellipticCurve(int(args[0]), int(args[1]), int(args[2]))
        curve.getInfo()
    except:
        print("\nthe arguments need to be integers! try again...")

else:
    print("\nyou need to enter a modulus and both a and b for the curve\nhere is an example\npy ellipticCurveGroupOperations.py p a b")

addition = pointAddition((1, 2), (9, 12))
addition.calculate()
