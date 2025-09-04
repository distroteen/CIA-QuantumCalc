from sympy import randprime, mod_inverse

def generate_prime(bits=512):
    from random import getrandbits
    n = getrandbits(bits)
    return randprime(2**(bits-1), 2**bits)

def modexp(base, exp, mod): return pow(base, exp, mod)
def invmod(a, m): return mod_inverse(a, m)
