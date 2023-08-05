import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

plt.rcParams['figure.figsize'] = 15, 8
plt.rcParams.update({'font.size': 10})

# define domain
# # domain for the function lies in between [0, L)
dx = 0.001
L = np.pi
x = L * np.arange(-1+dx, 1+dx, dx)
n = len(x)
nquart = int(n // 4)

# define hat function
f = np.zeros_like(x)
f[nquart: 2 * nquart] = (4 / n) * np.arange(1, nquart + 1)
f[2 * nquart : 3 * nquart] = np.ones(nquart) - (4 / n) * np.arange(0, nquart)

fig, ax = plt.subplots()
ax.plot(x, f, '-', color='k', linewidth=2)

# compute Fourier Series
name = 'Accent'
cmap = get_cmap('tab10')
colors = cmap.colors
ax.set_prop_cycle(color=colors)

A0 = np.sum(f * np.ones_like(x)) * dx
ffs = A0 / 2

discrete_val = 20
Ak = np.zeros(discrete_val)
Bk = np.zeros(discrete_val)

for k in range(discrete_val):
    Ak[k] = np.sum(f * np.cos(np.pi * (k + 1) * x / L)) * dx
    Bk[k] = np.sum(f * np.sin(np.pi * (k + 1) * x / L)) * dx
    ffs = ffs + Ak[k] * np.cos(np.pi * (k + 1) * x / L) + Bk[k] * np.sin(np.pi * (k + 1) * x / L)
    ax.plot(x, ffs, '-')

plt.show()