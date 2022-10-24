# import math
#
#
# z = [100,50]
#
# y = [4, 9, 14, 19, 24]
#
#
# d = []
#
#
# for yr in y:
#     print((yr-4, 50, (50/math.cos(math.atan(yr/50)))-50.16))
#
# print("\n")
#
# for yx in y:
#     print((yx-4, 100, 100/math.cos(math.atan(yx/100))))
import math

imWidth = 600
imHeight = 450
ballDiameter = 6.5


def mirror(x, y):
    return imWidth - x, y


def calcDepth(pxDiameter):
    x = pxDiameter
    depthZ = -0.0053 * (pow(x, 5)) + 0.5331 * (pow(x, 4)) - 31.2349 * (pow(x, 3)) + 1063.4490 * (
        pow(x, 2)) - 19565.6927 * (x) + 153717.6087
    return (depthZ)


def actualCoordinates(Xpx, Ypx, diameterpx, diameterpx2):
    xt, yt = mirror(Xpx, Ypx)

    depth = calcDepth(diameterpx)
    depth2 = calcDepth(diameterpx2)

    pxDistArb = Xpx - xt

    actualDistArb = (pxDistArb * 6.5) / diameterpx

    theta = 2 * (math.asin(actualDistArb / (2 * depth)))

    distanceBetweenEndPonits = pow(depth, 2) + pow(depth2, 2) + (2 * (depth * depth2) * math.cos(theta))

    return (distanceBetweenEndPonits)


g = 9.80


def get_val(R, T):
    n = math.atan(T * T * g / (2 * R))
    V = T * g / (2 * math.sin(n))

    return (n, V)


def get_v_d_comp(n, V, t):
    Vx = V * (math.cos(n))
    Vy = V * (math.sin(n)) - g * t

    dx = Vx * t
    dy = Vy * t

    return (Vx, Vy, dx, dy)


def max_h(V, n):
    H = ((V * math.sin(n)) ** 2) / (2 * g)

    return H


"""
Input
"""


T = input("Enter the time at which projectile starts : ")

