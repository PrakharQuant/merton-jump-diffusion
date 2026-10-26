"""Simple examples for the super-simplified Merton Jump Diffusion model."""

from merton import merton_call, merton_put, black_scholes_call

# Classic parameters
S = 100.0
K = 100.0
T = 1.0
r = 0.05
sigma = 0.2          # diffusion vol
lam = 1.0            # ~1 jump per year
mu_j = -0.10         # average log-jump (negative → crash bias)
sigma_j = 0.30       # jump size volatility

bs_price = black_scholes_call(S, K, T, r, sigma)
mjd_price = merton_call(S, K, T, r, sigma, lam, mu_j, sigma_j)
mjd_put_price = merton_put(S, K, T, r, sigma, lam, mu_j, sigma_j)

print("=== Super Simple Merton Jump Diffusion ===")
print(f"Black-Scholes Call : {bs_price:.4f}")
print(f"Merton JD Call     : {mjd_price:.4f}")
print(f"Jump Premium       : {mjd_price - bs_price:.4f}")
print(f"Merton JD Put      : {mjd_put_price:.4f}")
print()
print("Why higher? Jumps add extra risk that cannot be perfectly hedged.")
