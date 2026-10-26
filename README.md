# Super Simplified Merton Jump Diffusion

**Credit: Prakhar Gupta**  
bestofprakhar@gmail.com  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prakhar-gupta-5b7250372/)  [![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/PrakharQuant)

---

**Merton's Jump Diffusion is the massive, practical upgrade to Black-Scholes.**

Black-Scholes assumes prices move continuously and smoothly (geometric Brownian motion). Real markets jump — earnings surprises, crashes, news, tweets. Merton (1976) adds a Poisson jump process on top of the continuous diffusion. Result: fat tails, volatility smiles, and more realistic option prices, while still having a beautiful closed-form solution.

This repo super-simplifies the idea, the math, and the code so anyone can understand and use it in minutes.

## Quick Start

```python
from merton import merton_call, merton_put

price = merton_call(S=100, K=100, T=1.0, r=0.05, sigma=0.2, lam=1.0, mu_j=-0.1, sigma_j=0.3)
print(price)
```

## The Model in One Picture

Stock price = continuous Black-Scholes path **+** random jumps (Poisson arrivals, log-normal sizes).

## Live Demo

See the beautiful single-page explanation with interactive formula and code:  
**[GitHub Pages Site](https://prakharquant.github.io/simple-merton-jump-diffusion/)** (enable Pages in repo settings → Pages → Deploy from main branch / root)

## Files

- `index.html` — Beautiful, self-contained GitHub Pages site
- `merton.py` — Clean, minimal, production-ready Python implementation
- `example.py` — Simple usage examples

---

Made simple by Prakhar Gupta. Star the repo if this helped you!
