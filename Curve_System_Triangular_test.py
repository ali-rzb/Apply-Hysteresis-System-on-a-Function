import scipy.io
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import glob
from hysteresis_apply_function import hysteresis_apply

mat = scipy.io.loadmat('Data.mat')
begin_t = 0
end_t = 400
t = np.arange(begin_t, end_t, 1)
s = mat['val'][0][begin_t:end_t]
h = np.zeros(end_t - begin_t)
up_cut = 114
down_cut = 50
hysteresis_width = 25

for n in t:
    i = n - begin_t
    if i <= 200:
        s[i] = i
    else:
        s[i] = 400 - i


def up_way_function(_input):
    if _input >= up_cut:
        return up_cut
    elif (_input >= down_cut) & (_input <= up_cut):
        return (_input * 64 * 64 - 50 * 64 * 64) ** (1/3) + 50
    else:
        return down_cut


def down_way_function(_input):
    if _input >= up_cut:
        return up_cut
    elif (_input < up_cut) & (_input >= down_cut):
        return (_input/16 - 50/16) ** 3 + 50
    else:
        return down_cut

n = max(s) - min(s)
rng = range(min(s), max(s))
up_way_plot = np.zeros(n)

for i in rng:
    up_way_plot[i - min(s)] = up_way_function(i).real
down_way_plot = np.zeros(n)

for i in rng:
    down_way_plot[i - min(s)] = down_way_function(i).real


plt.subplot(2, 1, 1)
plt.plot(rng, up_way_plot, 'r', rng, down_way_plot)
plt.axis([min(s), max(s), down_cut - down_cut * 0.1, up_cut + down_cut * 0.1])
plt.grid(True)


h = hysteresis_apply(s, up_cut, down_cut, up_way_function, down_way_function)

# # fig = plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 2)
plt.plot(t, h, 'r', t, s)
plt.grid(True)
plt.axis([0, 400, 0, 200])
plt.savefig("Curve_System_Triangular_test.png")
plt.show()
