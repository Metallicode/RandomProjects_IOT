import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
from scipy.signal import find_peaks
import numpy as np
from matplotlib import pyplot as plt
import sounddevice as sd
import time

s_rate, signal = wavfile.read("string.wav") 

FFT = abs(scipy.fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))

min_peak_heigth = 300000
indices = find_peaks(FFT[range(len(FFT)//2)], height=min_peak_heigth, width=2)[0]
peaks = [freqs[x] for x in indices]

duration = 5.0
x = np.linspace(0, duration * 2 * np.pi, duration * s_rate)

wave_table = np.array(np.sin(peaks[0] * x))
for i in peaks[1:]:
      wave_table = wave_table + np.sin(i * x)

wave_table = wave_table * 0.02
sd.play(wave_table, s_rate)
time.sleep(duration)
sd.stop()

plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
plt.scatter(peaks,[min_peak_heigth for x in peaks] , c='red')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

wavfile.write("string_texture.wav", s_rate, wave_table)

plt.plot(wave_table)#plt.plot(signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

