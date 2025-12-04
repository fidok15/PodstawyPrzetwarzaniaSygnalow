import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

fs = 200
t = np.arange(0, 1, 1/fs)

func = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*15*t) + np.sin(2*np.pi*30*t)

order = 4
cutoff = 20
norm_cutoff = cutoff / (fs/2)

b, a = signal.butter(order, norm_cutoff, btype='low')
filtered_signal = signal.lfilter(b, a, func)

N = len(func)

fft_org = np.fft.fft(func)
fft_org_amp = (2/N) * np.abs(fft_org)

fft_filt = np.fft.fft(filtered_signal)
fft_filt_amp = (2/N) * np.abs(fft_filt)

freqs = np.fft.fftfreq(N, 1/fs)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.stem(freqs[:N//2], fft_org_amp[:N//2])
plt.title("FFT sygnał oryginalny")
plt.xlabel("f [Hz]")
plt.ylabel("A")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(freqs[:N//2], fft_filt_amp[:N//2])
plt.title("FFT sygnał przefiltrowany")
plt.xlabel("f [Hz]")
plt.ylabel("A")
plt.grid(True)

plt.tight_layout()
plt.show()