# on input
# p, a, b, P, Q
#
# process
# find all Elements to get the order
#

import sys
args = sys.argv[1:]


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

    def getElements(self):
        print(
            f"\nthe given elliptic curve has these points:\n{self.points}\nand an order of {len(self.points)}")


if len(args) == 3:
    try:
        curve = ellipticCurve(int(args[0]), int(args[1]), int(args[2]))
        curve.getElements()
    except:
        print("\nthe arguments need to be integers! try again...")

else:
    print("\nyou need to enter a modulus and both a and b for the curve\nhere is an example\npy ellipticCurveGroupOperations.py p a b")
