def sum(a, b):
    return a + b

def sqr(a):
    return a * a

def get_circle_area(r):
    import math
    return math.pi * sqr(r)

def max(a, b):
    if a > b:
        return a
    return b

def positive(a):
    return a > 0

def is_in_range(n, start, end):
    return n >= start and n <= end

def modul(a):
    if a < 0:
        return a * -1
    return a

def is_leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def max3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    return c

def integers(start, end):
    for n in range(start, end):
        print(n)

def su_range(start, end):
    return sum(range(start, end))