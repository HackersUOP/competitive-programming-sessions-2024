# Answer taken from https://github.com/thusharakart/Coding-Sessions

mod = 1000000000
def fib (n):
    if n == 0: return (0, 1)
    p = fib(n >> 1)
    c = ((p[0]%mod) * (2 * p[1] - p[0])%mod)%mod
    d = (pow(p[0],2)%mod  + pow(p[1],2)%mod)%mod
    if n&1: return (d, (c + d)%mod)
    return (c, d)
for i in range(int(input())):
    print(fib(int(input()))[0])
