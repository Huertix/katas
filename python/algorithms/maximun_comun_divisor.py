import sys

def naiveGCD(a, b):
    best = 0

    for index in range(1, a+b):
        if not index/a and not index/b:
            best = index

    return best

# Euclidean Algorithm
# gcd(a, b) = gcd(a', b) = gcd(b, a')

def euclidGCD(a, b):
    print a, b
    if b == 0:
        return a

    _a = a % b
    return euclidGCD(b, _a)


a, b = raw_input().split(" ")
a, b = int(a), int(b)
# print naiveGCD(a, b)
print euclidGCD(a, b)


# Recursive example
#
# euclidGCD(3918848, 1653264)
# =euclidGCD(1653264, 612320)
# =euclidGCD(612320, 428624)
# =euclidGCD(428624, 183696)
# =euclidGCD(183696, 61232)
# =euclidGCD(61232, 0)


