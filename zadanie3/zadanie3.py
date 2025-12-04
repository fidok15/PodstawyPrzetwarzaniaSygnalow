import numpy as np
import matplotlib.pyplot as plt

fs = 200
t = np.arange(0, 1, 1/fs)

signal = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*15*t) + np.sin(2*np.pi*30*t)

N = len(signal)
dft = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        dft[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)

moddtf = np.abs(dft) / N
freqs = np.arange(0, fs, fs/N)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(t, signal, label="sygnał złożony")
plt.title("sygnal w czasie")
plt.xlabel("czas")
plt.ylabel("amplituda")
plt.legend()
plt.grid(True)


plt.subplot(1,2,2)
plt.stem(freqs[:N//2], moddtf[:N//2])
plt.title("widmo amplitudowe")
plt.xlabel("czestotliowsc")
plt.ylabel("amplituda")
plt.grid(True)

plt.tight_layout()
plt.show()
