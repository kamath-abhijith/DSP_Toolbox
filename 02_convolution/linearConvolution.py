import numpy as np

from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style

import mysignals as sig

def linear_convolution(x,y):
	"""
	Computes the linear convolution
	of two discrete-time signals
	
	INPUT:  Input signals, x,y
	OUTPUT: Output signals, out

	Author: Abijith J. Kamath
	kamath-abhijith.github.io
	"""
	
	# Retrieve dimensions
	N = len(x)
	M = len(y)
	out = np.zeros(N+M)

	# Convolution sum
	for i in range(N):
		for j in range(M):
			out[i+j] = out[i+j] + x[i]*y[j]

	# Truncate to mode='same'
	out = out[int(np.floor(M/2)):N+int(np.floor(M/2))]

	return out

## Load signal
input_signal = sig.InputSignal_1kHz_15kHz
filter_response = sig.Impulse_response

## Compute convolution
output_signal = signal.convolve(input_signal,filter_response,mode='same')

output_signal_v2 = linear_convolution(input_signal,filter_response)

## Plots
style.use('ggplot')
style.use('dark_background')

f, plts = plt.subplots(3,sharex=True)

plts[0].plot(input_signal,color='blue',label='input')
plts[0].legend(loc='upper right')
plts[0].set_title('Input Signal')

plts[1].plot(filter_response,color='red',label='filter response')
plts[1].legend(loc='upper right')
plts[1].set_title('Filter Response')

plts[2].plot(output_signal,color='green',label='output signal scipy')
plts[2].plot(output_signal_v2,color='brown',label='output signal function')
plts[2].legend(loc='upper right')
plts[2].set_title('Output Signal')

plt.show()