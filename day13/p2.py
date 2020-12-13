"""
implementation of chinese remainder theorem from:
https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
"""
from functools import reduce
def chinese_remainder(n, a):
    sum_ = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum_ += a_i * mul_inv(p, n_i) * p
    return sum_ % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open('day13/input.txt') as f:
    f.readline()
    ids=[int(bus) if bus!='x' else bus for bus in f.readline().strip().split(',')]
a=[]
n=[]
for i,bus in enumerate(ids):
    if bus!='x':
        a.append((bus-i)%bus)
        n.append(bus)
print(chinese_remainder(n,a))