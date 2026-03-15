import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

t = np.linspace(0, 1, 1000)
eeg_signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2*np.pi*30*t) + 0.3*np.random.randn(1000)

#Filtering
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5*fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a , data)
    return y

#applying filter
fs = 1000 
alpha_only = butter_bandpass_filter(eeg_signal, 13, 30, fs)

#Plotting
plt.figure(figsize=(15, 6))
plt.plot(t, eeg_signal, label="Raw EEG (Mixed)", alpha=0.5)
plt.plot(t, alpha_only, label="Alpha Wave Only (13-30 Hz)", color='red', linewidth= 2)
plt.legend()
plt.title("Extracting Alpha Waves using Band-pass Filter")
plt.show()

