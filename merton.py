"""
Super simplified Merton Jump Diffusion option pricing.
Closed-form European call/put as Poisson-weighted sum of Black-Scholes prices.

Author: Prakhar Gupta (bestofprakhar@gmail.com)
"""

import math
from math import exp, log, sqrt, pi
from typing import Optional

# Normal CDF (accurate approximation, no scipy dependency)
def norm_cdf(x: float) -> float:
    """Abramowitz & Stegun approximation of the cumulative normal distribution."""
    if x < -8:
        return 0.0
    if x > 8:
        return 1.0
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    sign = 1 if x >= 0 else -1
    x = abs(x)
    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * exp(-x * x / 2)
    return 0.5 * (1.0 + sign * y)

def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Standard Black-Scholes European call."""
    if T <= 0 or sigma <= 0:
        return max(S - K * exp(-r * T), 0.0)
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return S * norm_cdf(d1) - K * exp(-r * T) * norm_cdf(d2)

def black_scholes_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Standard Black-Scholes European put."""
    if T <= 0 or sigma <= 0:
        return max(K * exp(-r * T) - S, 0.0)
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return K * exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)

def merton_call(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    lam: float,
    mu_j: float,
    sigma_j: float,
    n_terms: int = 50,
) -> float:
    """
    Merton Jump Diffusion European call price.

    Parameters
    ----------
    S : spot price
    K : strike
    T : time to maturity (years)
    r : risk-free rate
    sigma : diffusion volatility (continuous part)
    lam : jump intensity (expected jumps per year)
    mu_j : mean of log-jump size (ln(Y) ~ N(mu_j, sigma_j^2))
    sigma_j : std of log-jump size
    n_terms : truncation of Poisson sum (50 is plenty)
    """
    if T <= 0:
        return max(S - K, 0.0)

    # Expected relative jump size compensator
    k_bar = exp(mu_j + 0.5 * sigma_j ** 2) - 1.0
    lambda_prime = lam * (1.0 + k_bar)

    price = 0.0
    for n in range(n_terms):
        # Poisson probability (adjusted intensity)
        poisson = exp(-lambda_prime * T) * (lambda_prime * T) ** n / math.factorial(n)

        # Conditional volatility and rate given n jumps
        sigma_n = sqrt(sigma ** 2 + n * sigma_j ** 2 / T)
        r_n = r - lam * k_bar + n * (mu_j + 0.5 * sigma_j ** 2) / T

        price += poisson * black_scholes_call(S, K, T, r_n, sigma_n)

    return price

def merton_put(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    lam: float,
    mu_j: float,
    sigma_j: float,
    n_terms: int = 50,
) -> float:
    """Merton Jump Diffusion European put (via put-call parity)."""
    call = merton_call(S, K, T, r, sigma, lam, mu_j, sigma_j, n_terms)
    return call - S + K * exp(-r * T)

# Convenience aliases
mjd_call = merton_call
mjd_put = merton_put
