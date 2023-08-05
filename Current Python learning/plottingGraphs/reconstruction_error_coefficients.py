import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from fourier_series import A0, f, x, L, dx

plt.rcParams['figure.figsize'] = 20, 10
plt.rcParams.update({'font.size': 10})

ffs = (A0 / 2) * np.ones_like(f)
kmax = 100
Ak = np.zeros(kmax)
Bk = np.zeros(kmax)
ERR = np.zeros(kmax)

Ak[0] = A0 / 2
ERR[0] = np.linalg.norm(f - ffs) / np.linalg.norm(f)

for k in range(1, kmax):
    Ak[k] = np.sum(f * np.cos(np.pi * k * x / L)) * dx
    Bk[k] = np.sum(f * np.sin(np.pi * k * x / L)) * dx
    ffs += Ak[k] * np.cos(k * np.pi * x / L) + Bk[k] * np.sin(k * np.pi * x / L)
    ERR[k] = np.linalg.norm(f - ffs) / np.linalg.norm(f)

thresh = np.median(ERR) * np.sqrt(kmax) * (4 / np.sqrt(3))
r = np.max(np.where(ERR > thresh))

fig, ax = plt.subplots(2, 1)
ax[0].semilogy(np.arange(kmax), Ak, color='k', linewidth=2)
ax[0].semilogy(r, Ak[r], 'o', color='b', markersize=10)
plt.sca(ax[0])
plt.title("Fourier Coefficients")

ax[1].semilogy(np.arange(kmax), ERR, color='k', linewidth=2)
ax[1].semilogy(r, ERR[r], 'o', color='b', markersize=10)
plt.sca(ax[1])
plt.title('Error')

plt.show()