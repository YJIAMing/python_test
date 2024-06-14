def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def fab(a):
    if a == 0 or a == 1:
        return 1
    return fab(a - 1) + fab(a - 2)


def fab_loop(n):
    a = 1
    b = 1
    for i in range(1, n):
        res = a + b
        a = b
        b = res
    return res


print(gcd(6, 100))
print(fab(10))
print(fab_loop(10))  # test
# test new branch and merge
