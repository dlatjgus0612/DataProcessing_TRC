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

# Frequency y plt 
plt.figure(num=1, dpi=100, facecolor='white')       # 고유 번호 num 1, 해상도 100(적당)
plt.plot(t, y, 'r')
plt.xlim(0, 0.05)
plt.xlabel('time($sec$))')
plt.ylabel('y')
plt.savefig("data/fft_test_figure1.png", dpi=300)

# Caculate FFT ***
NFFT = len(y)                        # NFFT = len of signal
#NFFT = 2**int(np.ceil(np.log2(n)))                 # NFFT를 n 이상인 2의 제곱수로 설정하여 zero-padding
k = np.arange(NFFT)             # 0부터 NFFT-1까지의 정수 배열 (주파수 성분 인덱스)

# 1. 이산 주파수 범위 설정
f0 = k * Fs / NFFT                      # double sides frequency range
f0 = f0[range(math.trunc(NFFT/2))]      # single-sided frequency range
# f0 = f0[:NFFT//2]                     # 슬라이싱을 이용하여 앞의 절반만 취함

# 2. FFT 계산 및 단일 측면 주파수 범위 선택
Y = np.fft.fft(y) / NFFT                # FFT 수행 후 Nomalization 
Y = Y[range(math.trunc(NFFT/2))]        # single-sided frequency range

# 3. 주파수 성분의 진폭 및 위상 계산
amplitude_Hz = 2*abs(Y)               # 단일 측면 주파수 성분의 진폭 계산 (두 배로 보정)
phase_ang = np.angle(Y)*180/np.pi   # 각 주파수 성분의 위상을 도(degree)로 변환

# figure 1 
plt.figure(num=2, dpi=100, facecolor='white')
plt.subplots_adjust(hspace=0.6, wspace=0.3)
plt.subplot(3,1,1)
plt.plot(t, y, 'r')
plt.title('Singnal FFT analysis')
plt.xlabel('time($sec$)')
plt.ylabel('y')

# figure 2 
plt.subplot(3,1,2)
plt.plot(2 * f0, amplitude_Hz, 'r')   #단일 측면 주파수의 성분을 표현하기 위한 보정
plt.xlim(0, 200)
plt.ylim(0, 1.2)
plt.title('Single-Sided Amplitude Spectrum of y(t)')
plt.xlabel('frequency($Hz$)')
plt.ylabel('amplitude')
plt.grid()

# figure 3
plt.subplot(3,1,3)
plt.plot(2 * f0, phase_ang, 'r')      #단일 측면 주파수의 성분을 표현하기 위한 보정
plt.xlim(0, 200)
plt.ylim(-180, 180)
plt.title('Single-Sided Phase Spectrum of y(t)')
plt.xlabel('frequency($Hz$)')
plt.ylabel('phase($deg.$)')
plt.xticks([0, 60, 120, 200])
plt.yticks([-180, -90, 0, 90, 180])
plt.grid()

plt.show()
