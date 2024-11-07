import matplotlib.pyplot as plt
import numpy as np
import math 

# Define variables ***
St = 0.005                      # St : Sampling Time (샘플링 시간 간격)
Fs = 1 / St                     # Fs : Sampling Frequency (샘플링 주파수) = 2000Hz, 1초 동안 2000번 샘플링
T = 1 / Fs                      # T : Sampling Period (샘플링 주기) = 0.0005초
te = 0.5                        # te : Total Sampling Time (샘플링할 전체 시간 길이)

# Generating time vector
t = np.arange(0, te, T)         # t : Time Vector, 0초부터 te까지 T 간격으로 시간 배열 생성

# Define Noise 
noise = np.random.normal(0, 0.05, len(t))  # 평균 0, 표준편차 0.05인 가우시안 분포를 따르는 랜덤 값 생성

# Generate signal with two frequency components
# 60Hz 사인파 (진폭 0.6, 위상 π/2) + 120Hz 사인파 (진폭 1)
x = 0.6 * np.cos(2 * np.pi * 60 * t + np.pi / 2) + np.cos(2 * np.pi * 120 * t)
y = x + noise                   # Signal with added noise

# Plot the time-domain signal
plt.figure(num=1, dpi=100, facecolor='white')  # Figure with unique num, dpi=100
plt.plot(t, y, 'r')
plt.xlim(0, 0.05)
plt.xlabel('time ($sec$)')
plt.ylabel('y')
plt.savefig("data/fft_test_figure1.png", dpi=300)

# Perform FFT ***
NFFT = len(y)                     # NFFT : Number of data points (Signal length)
k = np.arange(NFFT)               # Array of integer indices from 0 to NFFT-1

# Define frequency range for single-sided spectrum
f0 = k * Fs / NFFT                # Double-sided frequency range
f0 = f0[:NFFT // 2]               # Single-sided frequency range (Nyquist range)

# Compute FFT and adjust for single-sided spectrum
Y = np.fft.fft(y) / NFFT          # Perform FFT and normalize
Y = Y[:NFFT // 2]                 # Single-sided frequency range (Nyquist range)

# Calculate amplitude and phase for frequency components
amplitude_Hz = 2 * abs(Y)         # Amplitude for single-sided spectrum (corrected by 2x)
phase_ang = np.angle(Y) * 180 / np.pi  # Convert phase to degrees

# Plot time-domain signal
plt.figure(num=2, dpi=100, facecolor='white')
plt.subplots_adjust(hspace=0.6, wspace=0.3)
plt.subplot(3, 1, 1)
plt.plot(t, y, 'r')
plt.title('Signal FFT Analysis')
plt.xlabel('time ($sec$)')
plt.ylabel('y')

# Plot single-sided amplitude spectrum
plt.subplot(3, 1, 2)
plt.plot(2 * f0, amplitude_Hz, 'r')  # Adjusted for single-sided frequency components
plt.xlim(0, 200)
plt.ylim(0, 1.2)
plt.title('Single-Sided Amplitude Spectrum of y(t)')
plt.xlabel('frequency ($Hz$)')
plt.ylabel('amplitude')
plt.grid()

# Plot single-sided phase spectrum
plt.subplot(3, 1, 3)
plt.plot(2 * f0, phase_ang, 'r')     # Adjusted for single-sided frequency components
plt.xlim(0, 200)
plt.ylim(-180, 180)
plt.title('Single-Sided Phase Spectrum of y(t)')
plt.xlabel('frequency ($Hz$)')
plt.ylabel('phase ($deg.$)')
plt.xticks([0, 60, 120, 200])
plt.yticks([-180, -90, 0, 90, 180])
plt.grid()

plt.show()
