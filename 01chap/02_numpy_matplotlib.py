# date : 2024.5.16, 북서태평양 해상에서
# made by : Peter
# file_name : matplotlib_test-1.py

from matplotlib import pyplot as plt
import numpy as np 

def draw_graph():
    x = np.arange(1, 10)
    y = x * 3

    # 3가지 산점도 
    plt.scatter(x, y, color='blue', marker = '+', s = 100) # s = 마커 크기
    plt.plot(x, y-2, linestyle=":", 
            color = 'blue', 
            marker = 'o',
            markeredgecolor = 'g',
            markerfacecolor = 'r'
            )
    plt.plot(x, y-5, linestyle="--", 
            color = 'black', 
            marker = 's',
            markeredgecolor = 'm',
            markerfacecolor = 'c'
            )

    plt.show()

def color_graph():
    x = np.arange(1, 10)
    y = x * 3

    # 3가지 산점도 
    plt.scatter(x, y, color='blue', marker = '+', s = 100) # s = 마커 크기
    plt.plot(x, y-2, linestyle=":", 
            color = 'blue', 
            marker = 'o',
            markeredgecolor = 'g',
            markerfacecolor = 'r'
            )
    plt.plot(x, y-5, linestyle="--", 
            color = 'black', 
            marker = 's',
            markeredgecolor = 'm',
            markerfacecolor = 'c'
            )

    plt.show()


draw_graph()
color_graph()
