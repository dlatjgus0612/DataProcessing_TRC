import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib import font_manager, rc

# 폰트 등록 강제 설정 
font_path = '/home/ish/fonts/NanumGothicBold.ttf'  # 확인된 폰트 경로 사용
font_prop = font_manager.FontProperties(fname=font_path)
font_manager.fontManager.addfont(font_path)  # 폰트를 강제 추가
rc('font', family=font_prop.get_name())

# 모든 옵션에서 nanumgothic 직접 지정 
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['font.sans-serif'] = [font_prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False # 마이너스 표시 

# 서브플롯 설정 (Cartopy 투영법 사용)
fig, axes = plt.subplots(1, 2, figsize=(16, 8), 
                         subplot_kw={'projection': ccrs.PlateCarree()})  # 기본 투영법 설정

'''
1. 캐나다 지도
'''
ax1 = axes[0]
ax1.set_extent([-67, -60, 43, 49.1], crs=ccrs.PlateCarree())  # 캐나다 범위 설정
ax1.add_feature(cfeature.COASTLINE, linewidth=1)
ax1.add_feature(cfeature.BORDERS, linestyle=':')
ax1.add_feature(cfeature.LAND, facecolor='green')

# 캐나다 지도 위도 경도 라인
gl = ax1.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.7, linestyle='--')
gl.top_labels = False
gl.right_labels = False

ax1.set_title('Canada Map', fontsize=16)

'''
2. 한국 지도
'''
ax2 = axes[1]
ax2.set_extent([123, 132.5, 32, 38.5], crs=ccrs.PlateCarree())  # 한국 범위 설정
ax2.add_feature(cfeature.COASTLINE, linewidth=1)
ax2.add_feature(cfeature.LAND, edgecolor='black', facecolor='none')
ax2.add_feature(cfeature.OCEAN, facecolor='lightblue')

# 명암 표현을 위한 고해상도 이미지 추가
ax2.stock_img()

# 한국 지도 위도 경도 라인
gl = ax2.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.7, linestyle='--')
gl.top_labels = False
gl.right_labels = False

# 위치 데이터
lon = [126.97806, 129.07556, 126.70528, 128.60250, 127.38500, 126.85306, 131.86956]
lat = [37.56667, 35.17944, 37.45639, 35.87222, 36.35111, 35.15972, 37.24078]
labels = ['Seoul', '부산', '인천', '대구', 'Daejeon', '광주', 'Dokdo']

# 위치 표시
for x, y, label in zip(lon, lat, labels):
    ax2.plot(x, y, 'r*', transform=ccrs.PlateCarree(), markersize=10)  # 점 표시
    ax2.text(x, y + 0.2, label, color='black', fontsize=10, transform=ccrs.PlateCarree(), 
             ha='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

ax2.set_title('South Korea and Nearby Locations', fontsize=16)

plt.tight_layout()  # 레이아웃 간격 조정
plt.show()
