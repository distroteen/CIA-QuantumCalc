import numpy as np
from scipy import stats

def normal_dist(mu, sigma, size=1000): return np.random.normal(mu, sigma, size)
def binomial_dist(n, p, size=1000): return np.random.binomial(n, p, size)
def monte_carlo(func, trials=10000):
    results = [func() for _ in range(trials)]
    return np.mean(results), np.std(results)
