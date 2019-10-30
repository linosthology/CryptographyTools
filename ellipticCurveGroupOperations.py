# with this script you can compute all the points of an elliptic curve and its order.
# you can also compute point addition or duplication
# with timing comparison you can compare the computing times between point duplication and addition
#
# on input it takes the modulus p, a and b of the curve
# python ellipticCurveGroupOperations p a b
#
# optionally you can input either one point for point duplication
# python ellipticCurveGroupOperations p a b x y
# or two points for point addition
# python ellipticCurveGroupOperations p a b x1 y1 x2 y2
#

import extendedEuclidian
import time
import random
import sys

# get inputs of the user
args = sys.argv[1:]


# timing comparison takes an integer which defines how many trial runs you want to do
# and outputs the computing times for both addition and duplication
# for the computations it generates random points of the group in each round
def timingComparison(n):

    timeAddition: float
    timeDuplication: float

    # addition
    start_time = time.time()
    for x in range(0, n, 1):
        P = curve.points[random.randrange(len(curve.points))]
        continues = False
        while(not continues):
            Q = curve.points[random.randrange(len(curve.points))]
            if Q != P:
                pointAddition(P, Q)
                continues = True
        timeAddition = (time.time() - start_time)

    # duplication
    start_time = time.time()
    for x in range(0, n, 1):
        P = curve.points[random.randrange(len(curve.points))]
        print(P)
        pointDuplication(P)
        timeDuplication = (time.time() - start_time)
    print("\ntimeAddition:\n" + str(timeAddition) + "\n" + "per addition: " +
          str(timeAddition/n) + "\ntimeDuplication:\n" + str(timeDuplication) + "\n" + "per duplication: " +
          str(timeDuplication/n))


# if you have a negative number, you can turn its into its positiveEquivalent
def turnPositive(mod, element):
    if element < 0:
        return mod + element
    else:
        return element


# an elliptic curve takes its modulus, a and b
# when you instantiate a curve it automatically generates its elements and order
class ellipticCurve:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b
        self.calculateOrder()

    # function for calculating the order of the curve
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

                    # if point exists, add it to the curves points
                    self.points.append((x, y))

        # set the order of the group after computing all the points
        self.order = len(self.points)

    # getInfo prints out information about the curve in the terminal
    def getInfo(self):
        print(
            f"\nthe given elliptic curve has these points:\n{self.points}\nand an order of {len(self.points)}")


# pointAddition takes a two Points and calculates the addition of those on instantiation
class pointAddition:
    def __init__(self, P, Q):
        self.P = P
        self.Q = Q

        # calculate the new point
        self.calculate()

    def calculate(self):
        gradient: int

        # check whether addition is possible
        if self.P == self.Q:
            print(
                "you can't do addition with the same point, you need to perform point duplication")
        else:

            # perform the addition
            divident = self.Q[1]-self.P[1] % curve.p
            diviser = self.Q[0]-self.P[0] % curve.p
            inverse = extendedEuclidian.getInverse(curve.p, diviser)
            gradient = divident*inverse % curve.p
            x = (gradient ** 2 - self.P[0] - self.Q[0]) % curve.p
            y = turnPositive(
                curve.p, ((gradient*(self.P[0]-x)-self.P[1]) % curve.p))

            # print out the new point
            print(f"\n{self.P} + {self.Q} is ({x}, {y})!")


# pointDuplication takes the point it has to duplicate and computes the duplication on instantiation
class pointDuplication:
    def __init__(self, P):
        self.P = P

        # perform the calculation of the duplication
        self.calculate()

    def calculate(self):
        gradient: int
        divident = (3*(self.P[0]**2) + curve.a) % curve.p
        diviser = 2 * self.P[1] % curve.p
        inverse = extendedEuclidian.getInverse(curve.p, diviser)
        gradient = divident*inverse % curve.p
        x = (gradient ** 2 - self.P[0] - self.P[0]) % curve.p
        y = turnPositive(
            curve.p, ((gradient*(self.P[0]-x)-self.P[1]) % curve.p))

        # print out the new point
        print(f"\n{self.P} + {self.P} is ({x}, {y})!")


# check whether a given point is an element of the curve
def pointExists(x, y):
    givenPoint = (x, y)
    isPoint = False
    for point in curve.points:
        if givenPoint == point:
            isPoint = True
    return isPoint


# 4a³ + 27b² != 0
def hasSinguarities(p, a, b):
    singularities = False
    if ((((4*(a**3))+(27*(b**2))) % p) == 0):
        singularities = True
        print((((4*(a**3))+(27*(b**2))) % p))
    return singularities


# process the input of the user and perform function calls here
if 3 <= len(args) <= 7:
    try:
        # the user has put in at least 3 points for the curve itself
        # check if the curve has singularities
        curveHasSingularities = hasSinguarities(
            int(args[0]), int(args[1]), int(args[2]))

        if curveHasSingularities:
            print("the given elliptic curve has singularities!")
        else:

            # if the curve has no singularities, instantiate a curve
            curve = ellipticCurve(int(args[0]), int(args[1]), int(args[2]))

            # print the information about the curve
            curve.getInfo()

            # call timing comparison
            timingComparison(100)

            # the user put in 4 arguments
            if len(args) == 4:
                print("\na point needs a x and a y value")

            # the user put in 5 arguments, compute point duplication
            elif len(args) == 5:
                x = int(args[3])
                y = int(args[4])

                # check if the point the user put in exists
                if pointExists(x, y):
                    pointDuplication((x, y))
                else:
                    print("the given point is not an element of the group")

            # the user put in 6 arguments
            elif len(args) == 6:
                print("\na point needs a x and a y value")

            # the user put in 6 arguments, compute point addition
            elif len(args) == 7:

                # P
                x1 = int(args[3])
                y1 = int(args[4])

                # Q
                x2 = int(args[5])
                y2 = int(args[6])

                # check if the points the user put in exist
                if pointExists(x1, y1) and pointExists(x2, y2):
                    pointAddition((x1, y1), (x2, y2))
                else:
                    print("one of the given points is not an element of the group")

    # the user did not put ins integers, throw exception
    except:
        print("\nthe arguments need to be integers! try again...")

# the user did not put in enough or too many arguments, explain how to use the script
else:
    print("\nyou need to enter a modulus and both a and b for the curve\nhere is an example\npy ellipticCurveGroupOperations.py p a b")
    print("\nyou can also enter two or four more arguments to perform point duplication or addition with them")
