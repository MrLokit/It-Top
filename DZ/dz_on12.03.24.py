# s - global
s = 0
def sqw_abc(a,b,c):
    def sqw_de(d,e):
        return d*e
    global s
    s = 2*(sqw_de(a,b) + sqw_de(a,c) + sqw_de(b,c))
    return s

sqw_abc(2,4,6)
print(s)
sqw_abc(5,8,2)
print(s)
sqw_abc(1,6,8)
print(s)



print('\n')
# s - nonlocal
def sqw_abc(a,b,c):
    s = 0
    def sqw_de(d,e):
        nonlocal s
        s += d * e
    sqw_de(a,b)
    sqw_de(a,c)
    sqw_de(b,c)
    return 2 * s


print(sqw_abc(2,4,6))
print(sqw_abc(5,8,2))
print(sqw_abc(1,6,8))

