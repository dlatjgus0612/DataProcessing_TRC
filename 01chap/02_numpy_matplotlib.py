from matplotlib import pyplot as plt
import numpy as np 

def draw_graph():
    x = np.arange(1, 10)
    y = x * 3

    # 3가지 산점도 
    plt.scatter(x, y, color='blue', marker='+', s=100)  # s = 마커 크기
    plt.plot(x, y-2, linestyle=":", 
             color='blue', 
             marker='o',
             markeredgecolor='g',
             markerfacecolor='r'
             )
    plt.plot(x, y-5, linestyle="--", 
             color='black', 
             marker='s',
             markeredgecolor='m',
             markerfacecolor='c'
             )

    plt.show()

def color_graph():
    cmaps = plt.colormaps()  # Matplotlib에서 지원하는 모든 색상표 가져오기
    for cmap in cmaps:       # 리스트를 반복
        print(cmap)
        
    data = np.random.rand(10, 10)  # 예시 데이터 생성
    
    plt.imshow(data, cmap='viridis')  # 출력
    plt.colorbar()
    plt.title('Example with Viridis Colormap')
    plt.show()

def sub_graph():
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    ax1 = plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.title('1st Graph')
    plt.ylabel('Damped oscillation')

    #plt.xticks(visible = False) # Hide x-ticks and labels
    ax2 = plt.subplot(2, 1, 2, sharex=ax1)  # Sharing x-axis with ax1
    plt.plot(x2, y2, '.-')
    plt.title('2nd Graph')
    plt.xlabel('time (s)')
    plt.ylabel('undamped')
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()
    
def grid_graph():
    plt.figure(figsize=(10, 12)) 
    ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)   
    ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)   
    ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)   
    ax4 = plt.subplot2grid((3,3), (2,0))   
    ax5 = plt.subplot2grid((3,3), (2,1))   
    plt.show()


draw_graph()
color_graph()
sub_graph()
grid_graph()
