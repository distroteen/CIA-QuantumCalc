from decimal import Decimal, getcontext

getcontext().prec = 100  # Alta precisão

def add(a, b): return Decimal(a) + Decimal(b)
def sub(a, b): return Decimal(a) - Decimal(b)
def mul(a, b): return Decimal(a) * Decimal(b)
def div(a, b): return Decimal(a) / Decimal(b)
def power(a, b): return Decimal(a) ** Decimal(b)
def sqrt(a): return Decimal(a).sqrt()
