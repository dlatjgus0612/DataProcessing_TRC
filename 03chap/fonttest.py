import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

'''1. plot 확인 '''

# import numpy as np

# data = np.random.randint(-100, 100, 50).cumsum()
# plt.plot(range(50), data, 'r')
# mpl.rcParams['axes.unicode_minus'] = False
# plt.title('시간별 가격 추이')
# plt.ylabel('주식 가격')
# plt.xlabel('시간(분)')
# plt.show()

'''2. 버전 체크 '''

print ('버전: ', mpl.__version__)
print ('설치 위치: ', mpl.__file__)
print ('설정 위치: ', mpl.get_configdir())
print ('캐시 위치: ', mpl.get_cachedir())
print ('설정 파일 위치: ', mpl.matplotlib_fname())
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# ttf 폰트 전체개수
print(len(font_list))

f = [f.name for f in fm.fontManager.ttflist]
print(len(font_list))
# 10개의 폰트 명 만 출력
print(f[:79])
print([(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name])

'''
버전:  3.8.4
설치 위치:  /home/ish/.local/lib/python3.10/site-packages/matplotlib/__init__.py
설정 위치:  /home/ish/.config/matplotlib
캐시 위치:  /home/ish/.cache/matplotlib
설정 파일 위치:  /home/ish/.local/lib/python3.10/site-packages/matplotlib/mpl-data/matplotlibrc
79
'''

