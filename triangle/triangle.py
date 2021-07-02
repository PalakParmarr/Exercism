def equilateral(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return checktri(a, b, c) and a > 0 and a == b and a == c


def isosceles(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return checktri(a, b, c) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return checktri(a, b, c) and a != b and a != c and b != c

def checktri(a, b, c):
    return a + b > c and b + c > a and c + a > b