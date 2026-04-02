# -*- coding: utf-8 -*-
def classifyTriangle(a, b, c):
    # BUG FIX 1: moved isinstance check first so strings don't crash numeric comparisons
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # BUG FIX 2: was "b <= b" (always True), changed to "b <= 0"
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # BUG FIX 3: corrected triangle inequality — original formula was wrong
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # BUG FIX 4: was "a == b and b == a" — never checked c
    if a == b and b == c:
        return 'Equilateral'

    # BUG FIX 5: was (a*2)+(b*2)==(c*2) — used multiply not power, and didn't sort sides
    sides = sorted([a, b, c])
    x, y, z = sides
    if (x**2 + y**2) == z**2:
        return 'Right'

    # BUG FIX 6: was "a != b and b != c and a != b" — checked a!=b twice, missed a!=c
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'