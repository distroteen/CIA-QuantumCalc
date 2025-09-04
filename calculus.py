import sympy as sp

def derivative(expr, var): return sp.diff(expr, var)
def integral(expr, var): return sp.integrate(expr, var)
def limit(expr, var, point): return sp.limit(expr, var, point)
def series(expr, var, point=0, n=6): return sp.series(expr, var, point, n)
