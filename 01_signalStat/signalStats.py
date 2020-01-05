import numpy as np

from matplotlib import pyplot as plt
from matplotlib import style

def signal_mean(input_signal):
	_mean = 0.0
	N = len(input_signal)

	for x in range(N):
		_mean = _mean + input_signal[x]

	_mean = _mean / N
	return _mean

def signal_variance(input_signal):
	_variance = 0.0
	_mean = signal_mean(input_signal)
	N = len(input_signal)

	for x in range(N):
		_variance = _variance + (input_signal[x] - _mean)**2

	_variance = _variance / (N)
	return _variance

x = np.arange(0,1,0.01)
y1 = np.sin(2*np.pi*x)
y2 = np.cos(2*np.pi*x)

print(signal_mean(y1))
print(np.mean(y1))

print(signal_variance(y1))
print(np.var(y1))

style.use('ggplot')
style.use('dark_background')

f, plts = plt.subplots(2,sharey=True)

plts[0].plot(x,y1,label='sin')
plts[0].plot(x,y2,label='cos')
plts[0].legend()
plts[0].set_title('Sine and Cosine')

plts[1].plot(x,y1+0.5*y2,label='sin + cos')
plts[1].legend()
plts[1].set_title('Sine + Cosine')

plt.show()