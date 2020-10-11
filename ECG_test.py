import scipy.io
import matplotlib.pyplot as plt
import numpy as np
from hysteresis_apply_function import hysteresis_apply

mat = scipy.io.loadmat('Data.mat')
begin_t = 0
end_t = 1000
t = np.arange(begin_t, end_t, 1)
s = mat['val'][0][begin_t:end_t]
up_cut = 1180
down_cut = 926
hysteresis_width = 50


def up_way_function(_input):
    m = (up_cut - down_cut) / (up_cut - (down_cut + hysteresis_width))
    b = down_cut - m * down_cut
    if _input >= up_cut - hysteresis_width:
        return up_cut
    elif (_input >= down_cut) & (_input <= up_cut - hysteresis_width):
        return m * _input + b
    else:
        return down_cut


def down_way_function(_input):
    m = (up_cut - down_cut) / (up_cut - (down_cut + hysteresis_width))
    b = down_cut - m * (down_cut + hysteresis_width)
    if _input >= up_cut:
        return up_cut
    elif (_input < up_cut) & (_input >= down_cut + hysteresis_width):
        return m * _input + b
    else:
        return down_cut


n = max(s) - min(s)
rng = range(min(s), max(s))
up_way_plot = np.zeros(n)

for i in rng:
    up_way_plot[i - min(s)] = up_way_function(i)
down_way_plot = np.zeros(n)

for i in rng:
    down_way_plot[i - min(s)] = down_way_function(i)

plt.subplot(2, 1, 1)
plt.plot(rng, up_way_plot, 'r', rng, down_way_plot)
plt.axis([min(s), max(s), down_cut - down_cut * 0.01, up_cut + down_cut * 0.01])
plt.grid(True)

h = hysteresis_apply(s, up_cut, down_cut, up_way_function, down_way_function)

plt.subplot(2, 1, 2)
plt.plot(t, h, 'r', t, s)
plt.grid(True)
plt.axis([400, 500, 900, 1280])
plt.savefig("ECG_test.png")
fig = plt.figure(figsize=(12, 10))
plt.show()
