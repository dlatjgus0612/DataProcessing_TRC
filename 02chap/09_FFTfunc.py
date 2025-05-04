import matplotlib.pyplot as plt
import numpy as np
import math

# Define variables ***
St = 0.005                      # St : Sampling Time (샘플링 시간 간격)
Fs = 1 / St                     # Fs : Sampling Frequency (샘플링 주파수) = 2000Hz, 1초 동안 2000번 샘플링
T = 1 / Fs                      # T : Sampling Period (샘플링 주기) = 0.0005초
te = 0.5                        # te : Sampling interval time (샘플링할 전체 시간 길이)

# Generating frequency arrays over time
t = np.arange(0, te, T)         # t : Time Vector, 0초부터 te까지 T 간격으로 시간 배열 생성

# Define Noise (평균 0, 표준편차 0.05인 가우시안 분포를 따르는 랜덤 값, 길이는 t와 동일)
noise = np.random.normal(0, 0.05, len(t))

# Frequency x (두 가지 주파수 성분을 더한 신호)
# 60Hz 사인파 (진폭 0.6, 위상 π/2) + 120Hz 사인파 (진폭 1)
x = 0.6 * np.cos(2 * np.pi * 60 * t + np.pi / 2) + np.cos(2 * np.pi * 120 * t)
y = x + noise                   # Frequency y = x + noise

# Caculate FFT ***
n = len(y)                      # y = length of signal
NFFT = n                        # NFFT = len of signal
# NFFT = 2**int(np.ceil(np.log2(n)))  # Optionally use zero-padding
k = np.arange(NFFT)             # 0부터 NFFT-1까지의 정수 배열 (주파수 성분 인덱스)

# 1. 이산 주파수 범위 설정
f0 = k * Fs / NFFT                      # double sides frequency range
f0 = f0[range(math.trunc(NFFT/2))]      # single-sided frequency range

# 2. FFT 계산 및 단일 측면 주파수 범위 선택
Y1 = np.fft.fft(y) / NFFT                # FFT 수행 후 Nomalization
Y1 = Y1[range(math.trunc(NFFT/2))]       # single-sided frequency range

Y2 = np.fft.fft(y, NFFT)                 # zero-padding 후 FFT
Y2 = Y2[range(math.trunc(NFFT/2))]       # single-sided frequency range

Y3 = np.fft.fft(y, NFFT) / NFFT          # zero-padding 후 FFT 정규화
Y3 = Y3[range(math.trunc(NFFT/2))]       # single-sided frequency range

# 3. 주파수 성분의 진폭 및 위상 계산
amplitude_Y1 = 2 * abs(Y1)               # Y1의 진폭 계산
amplitude_Y2 = 2 * abs(Y2)               # Y2의 진폭 계산
amplitude_Y3 = 2 * abs(Y3)               # Y3의 진폭 계산

phase_Y1 = np.angle(Y1) * 180 / np.pi    # Y1의 위상 계산 (도 단위)
phase_Y2 = np.angle(Y2) * 180 / np.pi    # Y2의 위상 계산 (도 단위)
phase_Y3 = np.angle(Y3) * 180 / np.pi    # Y3의 위상 계산 (도 단위)

# 1. 진폭 및 위상 스펙트럼을 위한 subplot
plt.figure(num=2, dpi=100, facecolor='white')

# 서브플롯 1: Y1 진폭
plt.subplot(3, 2, 1)  # 3행 2열의 첫 번째 subplot
plt.plot(f0, amplitude_Y1, label='Y1 (np.fft.fft(y) / NFFT)', color='blue')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Amplitude Spectrum of Y1')
plt.grid(True)

# 서브플롯 2: Y1 위상
plt.subplot(3, 2, 2)  # 3행 2열의 두 번째 subplot
plt.plot(f0, phase_Y1, label='Y1 Phase', color='blue')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.legend()
plt.title('Phase Spectrum of Y1')
plt.grid(True)

# 서브플롯 3: Y2 진폭
plt.subplot(3, 2, 3)  # 3행 2열의 세 번째 subplot
plt.plot(f0, amplitude_Y2, label='Y2 (np.fft.fft(y, NFFT))', color='green')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Amplitude Spectrum of Y2')
plt.grid(True)

# 서브플롯 4: Y2 위상
plt.subplot(3, 2, 4)  # 3행 2열의 네 번째 subplot
plt.plot(f0, phase_Y2, label='Y2 Phase', color='green')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.legend()
plt.title('Phase Spectrum of Y2')
plt.grid(True)

# 서브플롯 5: Y3 진폭
plt.subplot(3, 2, 5)  # 3행 2열의 다섯 번째 subplot
plt.plot(f0, amplitude_Y3, label='Y3 (np.fft.fft(y, NFFT) / NFFT)', color='orange')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Amplitude Spectrum of Y3')
plt.grid(True)

# 서브플롯 6: Y3 위상
plt.subplot(3, 2, 6)  # 3행 2열의 여섯 번째 subplot
plt.plot(f0, phase_Y3, label='Y3 Phase', color='orange')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.legend()
plt.title('Phase Spectrum of Y3')
plt.grid(True)

# 그래프 간 간격 자동 조정
plt.tight_layout()
plt.show()

# Print numerical results for each Y
print("FFT Results for Y1 (np.fft.fft(y) / NFFT):")
print("Amplitude:", amplitude_Y1)
print("Phase:", phase_Y1)

print("\nFFT Results for Y2 (np.fft.fft(y, NFFT)):")
print("Amplitude:", amplitude_Y2)
print("Phase:", phase_Y2)

print("\nFFT Results for Y3 (np.fft.fft(y, NFFT) / NFFT):")
print("Amplitude:", amplitude_Y3)
print("Phase:", phase_Y3)

# Compare Y1 and Y2, Y2 and Y3, Y1 and Y3 using np.allclose()
print("\nIs Y1 approximately equal to Y2? ", np.allclose(Y1, Y2))
print("Is Y2 approximately equal to Y3? ", np.allclose(Y2, Y3))
print("Is Y1 approximately equal to Y3? ", np.allclose(Y1, Y3))
