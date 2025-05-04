from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 2개의 서브플롯 생성
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# 첫 번째 서브플롯 (shadedrelief)
m1 = Basemap(width=2000000, height=1800000, projection='lcc',
             resolution=None, lat_1=22, lat_2=50, lat_0=36, lon_0=124, ax=ax1)
m1.shadedrelief()
ax1.set_title('Shaded Relief')

# 두 번째 서브플롯 (etopo)
m2 = Basemap(width=2000000, height=1800000, projection='lcc',
             resolution=None, lat_1=22, lat_2=50, lat_0=36, lon_0=124, ax=ax2)
m2.etopo()
ax2.set_title('ETOPO')

# 서브플롯 간격 조정
plt.tight_layout()
plt.show()