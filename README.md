

# DataProcessing_TRC
for Marine-Meteorological-WindEnergy

## File Structure

    file structureDataProcessing_TRC
	 ┣ 01chap
	 ┃ ┣ 01_pandasbasic.py
	 ┃ ┣ 02_numpy_matplotlib.py
	 ┃ ┣ 03_histogram.py
	 ┃ ┣ 04_pythonbasic.py
	 ┃ ┣ 05_netcdf.py
	 ┃ ┗ 06_netcdf_eastsea.py
	 ┣ 02chap
	 ┃ ┣ 01_timeseries.py
	 ┃ ┣ 02_ulsandata.py
	 ┃ ┣ 03_wind_wave.py
	 ┃ ┣ 04_covariance.py
	 ┃ ┣ 05_linear_R.py
	 ┃ ┣ 06_rmse.py
	 ┃ ┣ 07_r2score.py
	 ┃ ┣ 08_r2score_graph.py
	 ┃ ┣ 09_FFT.py
	 ┃ ┣ 09_FFTfunc.py
	 ┃ ┣ 10_windtomath.py
	 ┃ ┣ 11_wind_16.py
	 ┃ ┣ 11_wind_buoydata.py
	 ┃ ┣ 11_wind_plot.py
	 ┃ ┣ 12_ulsan_windrose.py
	 ┃ ┣ 12_windrose.py
	 ┃ ┣ 13_buoydata_plot.py
	 ┃ ┣ 13_buoydata_plottest.py
	 ┃ ┣ 14_wave_monthly.py
	 ┃ ┣ 14_wave_monthly2.py
	 ┃ ┣ 14_wave_yearly_seasonal.py
	 ┃ ┗ 15_sun_monthly.py
	 ┣ 03chap
	 ┃ ┣ 01_cartesian_polar_plot.py
	 ┃ ┣ 02_cartesian_polar_exam.py
	 ┃ ┣ 03_polygon_test.py
	 ┃ ┣ 04_contour.py
	 ┃ ┣ 05_basemap_start.py
	 ┃ ┣ 05_basemap_start_cartopy.py
	 ┃ ┣ 06_basemap_hfradar.py
	 ┃ ┣ 06_basemap_hfradar_all.py
	 ┃ ┣ 06_basemap_hfradar_allclass.py
	 ┃ ┣ 06_basemap_hfradar_class.py
	 ┃ ┣ 06_basemap_ocean_obs.py
	 ┃ ┣ 07_basemap_polygon.py
	 ┃ ┣ 08_plot_slp_wind_class.py
	 ┃ ┣ 08_plot_slp_windvector.py
	 ┃ ┣ 08_plot_sst_basemap.py
	 ┃ ┣ 08_weather_basemap_2023.py
	 ┃ ┣ 09_KHOA_depth_base.py
	 ┃ ┣ 09_KHOA_depth_con.py
	 ┃ ┣ 10_basemap_landshape.py
	 ┃ ┣ 11_sand_polygon_base.py
	 ┃ ┣ 12_windvector_quiver.py
	 ┃ ┣ analysis_grib.py
	 ┃ ┣ analysis_pygrib.ipynb
	 ┃ ┣ analysis_pygrib.py
	 ┃ ┣ analysis_pygrib_colab.ipynb
	 ┃ ┣ fonttest.py
	 ┃ ┗ lookup_ncfile.py
	 ┣ 03chap_2
	 ┃ ┣ 01_pygmttest.py
	 ┃ ┣ 02_trackline.py
	 ┃ ┣ 03_etopo.py
	 ┃ ┣ 03_etopo_kr.py
	 ┃ ┣ 04_khoa_depth.py
	 ┃ ┣ 05_study_KOON.py
	 ┃ ┗ 05_study_pohang.py
	 ┣ data
	 ┃ ┗ related datasets…
	 ┣ README.md
	 ┣ gitsetting.sh
	 ┣ requirements.txt
	 ┣ setup.sh
	 ┗ tmux_checkgpu.py


## Usage
((used models or tools))

## Getting Started

    # 이거 하나면 된다 
    bash setup.sh
    # 환경 적용한 후 추가 수정 및 깃헙 관리를 할 예정이라면
    bash gitsetting.sh

(추가예정) 

> 안되는 라이브러리 있으면 그때 그때 추가로 깔아주세용 (최대한 requirments에 업데이트 예정)


## Links
- python을 이용한 해양. 기상. 풍력 자료처리 by 유학렬, 한진현, 김동환 (0.72)
- 개인 [NOTION](https://imsh.notion.site/1-python-750753d5ce7246d38846fb27a4e99829?pvs=4) (필요시 공유 드림니다 : 유료가 아니라 다 못엶)
- 개인 [TISTORY](https://imsh0206.tistory.com/category/Data%20Engineering%20%EC%9E%AC%EB%B0%8C%EB%94%B0/Ocean%20Meteorological%20Data) (이해하기 쉽게 더 풀어쓰려고 노력중)

