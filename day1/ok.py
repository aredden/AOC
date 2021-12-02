import cupy as np
from time import time
from performance_monitor import performance

@performance
def perf_func():
	for i in range(1000):
		arr = np.random.random(size=2**16)
		fft = np.fft.fft(arr)
		new_arr = np.fft.ifft(fft)
perf_func()