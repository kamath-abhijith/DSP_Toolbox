import numpy as np

from matplotlib import pyplot as plt
from matplotlib import style

import mysignals as sig

def discrete_fourier_transform(x,N):
	out_re = np.zeros(N)
	out_im = np.zeros(N)

	for k in range(N):
		for i in range(N):
			out_re[k] = out_re[k] + x[i]*np.cos(2*np.pi*k*i/N)
			out_im[k] = out_im[k] - x[i]*np.sin(2*np.pi*k*i/N)

	return out_re, out_im

## Construct signals
t = np.arange(0,1,0.01)

x = np.sin(2*np.pi*t) + 0.5*np.cos(2*np.pi*10*t)
# x = sig.InputSignal_1kHz_15kHz

## Compute DFT
x_hat_re, x_hat_im = discrete_fourier_transform(x,len(x))

x_hat_mag = np.zeros(len(x_hat_im))
for i in range(len(x_hat_im)):
	x_hat_mag[i] = np.sqrt(x_hat_re[i]**2 + x_hat_im[i]**2)

## Plots
style.use('ggplot')
style.use('dark_background')

plt.figure()
plt.plot(x)

f, plts = plt.subplots(3,sharex=True)
plts[0].stem(x_hat_re)
plts[1].stem(x_hat_im)
plts[2].stem(x_hat_mag)

plt.show()