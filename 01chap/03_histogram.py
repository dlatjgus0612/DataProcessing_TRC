from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
import numpy.random as random

def histogram():
    data = {'values' : [1, 2, 2, 2.5, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]}
    df = pd.DataFrame(data)
    # make histogram
    plt.hist(df['values'], color= 'y', edgecolor = 'white', alpha = 0.7, bins = 5)
    # 색, 투명도, 경계, 구간 지정 (0.7씩 5개로 표현)
    plt.title('Histogram Example')
    plt.xlabel('Values')
    plt.ylabel('Counts')

    print(df['values'].describe())
    plt.show()

def histogram2():
    data = np.random.normal(7, 3, 100)

    # 각 구간 데이터 개수, 구간 경계값 정의, 히스토그램 막대에 대한 객체 리스트 
    bin_interval = 2
    #counts, bins, patches = plt.hist(data, bins=[0,3,6,9,12,15], edgecolor = 'black')
    counts, bins, patches = plt.hist(data, 
                                     bins=np.arange(min(data), max(data) + bin_interval, bin_interval), 
                                     edgecolor = 'black')
    plt.xlabel("bins", fontsize = 12)
    plt.ylabel("count", fontsize = 12)

    for i in range(len(counts)):
        print(f"구간 {bins[i]:.2f}{bins[i+1]:.2f}: {counts[i]}개")

    plt.tight_layout()
    plt.show()

def mathwithhist():
    data = np.random.normal(7, 3, 100)

    # data point 에 대한 내림, 올림 계산
    floored_data = np.floor(data)
    ceiled_data = np.ceil(data)
    min_val = np.min(floored_data)
    max_val = np.max(ceiled_data)

    bin_interval = 2
    #counts, bins, patches = plt.hist(data, bins=[0,3,6,9,12,15], edgecolor = 'black')
    counts, bins, patches = plt.hist(data, 
                                     bins=np.arange(min_val, max_val + bin_interval, bin_interval), 
                                     edgecolor = 'black')
    plt.xlabel("bins", fontsize = 12)
    plt.ylabel("count", fontsize = 12)
    plt.grid(True)

    for i in range(len(counts)):
        print(f"구간 {bins[i]:.2f}{bins[i+1]:.2f}: {counts[i]}개")

    plt.tight_layout()
    plt.show()


histogram()
histogram2()
mathwithhist()