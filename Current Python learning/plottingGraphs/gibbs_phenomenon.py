import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib import animation, rc
from IPython.display import HTML

plt.rcParams['figure.figsize'] = 15, 8
plt.rcParams.update({'font.size': 18})
plt.rcParams['animation.html'] = 'jshtml'
plt.rcParams['animation.ffmpeg_path'] = ' c:\\users\\liyak\\appdata\\local\\pip\\cache\\wheels\\56\\30\\c5\\576bdd729f3bc062d62a551be7fefd6ed2f761901568171e4e'

dx = 0.01
L = 2 * np.pi
x = np.arange(0, L + dx, dx)
n = len(x)
nquart = int(np.floor(n / 4))

f = np.zeros_like(x)
f[nquart : 3 * nquart] = 1

A0 = np.sum(f * np.ones_like(x)) * dx * 2 / L
ffs = A0 / 2 * np.ones_like(f)

fig, ax = plt.subplots()
plt.plot(x,f,color='k', linewidth=2)
ffs_plot, = plt.plot([], [], color='r', linewidth=2)

all_ffs = np.zeros((len(ffs), 101))
all_ffs[:, 0] = ffs

for k in range(1, 101):
    Ak = np.sum(f * np.cos(2 * np.pi * k * x / L)) * dx * 2 / L
    Bk = np.sum(f * np.sin(2 * np.pi * k * x / L)) * dx * 2 / L
    ffs += Ak * np.cos(2 * np.pi * k * x / L) + Bk * np.sin(2 * np.pi * k * x / L)
    all_ffs[:, k] = ffs

def init():
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(-.2, 1.2)
    return ffs

def animate(iter):
    ffs_plot.set_data(x, all_ffs[:iter])
    return ffs_plot

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=101, interval=.5)
HTML(anim.to_html5_video())
