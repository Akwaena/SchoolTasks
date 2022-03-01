def conunction(n, k):
    n = bin(n)[2:]
    k = bin(k)[2:]
    s = ''
    if len(n) != len(k):
        if len(n) > len(k):
            k = '0' * (len(n) - len(k)) + k
        else:
            n = '0' * (len(k) - len(n)) + n
    for i in range(len(n)):
        if n[i] == k[i] == '1':
            s += '1'
        else:
            s += '0'
    return int(s,2)

def implication(x, y): return not x or y

def f(A):
    for x in range(10000):
        if not implication(conunction(x, 41) == 0, implication(conunction(x, 119) != 0,conunction(x, A) != 0)):
            return False
    return A


for i in range(100):
    if f(i)!=False: print(i)
