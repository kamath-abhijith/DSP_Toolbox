import numpy as np

from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style

import mysignals as sig

def signal_convolution(input_signal,filter_response):
	N = len(input_signal)
	M = len(filter_response)
	output_signal = np.zeros(N+M)

	for x in range(N):
		for y in range(M):
			output_signal[x+y] = output_signal[x+y] + input_signal[x]*filter_response[y]

	output_signal = output_signal[int(np.floor(M/2)):N+int(np.floor(M/2))]

	return output_signal

## Load signal
input_signal = sig.InputSignal_1kHz_15kHz
filter_response = sig.Impulse_response

## Compute convolution
output_signal = signal.convolve(input_signal,filter_response,mode='same')

output_signal_v2 = signal_convolution(input_signal,filter_response)

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