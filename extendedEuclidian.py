def egcd(mod, findInverseTo):
    if mod == 0:
        return (findInverseTo, 0, 1)
    else:
        gcd, x, y = egcd(findInverseTo % mod, mod)
        return (gcd, y - (findInverseTo//mod) * x, x)


def getInverse(mod: int, findInverseTo: int) -> int:
    _, _, inverse = egcd(mod, findInverseTo)
    if inverse < 0:
        return mod + inverse
    else:
        return inverse
