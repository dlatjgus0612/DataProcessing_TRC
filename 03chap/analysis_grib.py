import xarray as xr
import cfgrib

# 파일 경로 설정
file_path = "data/gdas1.fnl0p25.2024082100.f09.grib2"

# 모든 메시지 읽기
messages = cfgrib.open_file(file_path)

# 데이터 요약
print("파일 내 변수 요약:")
for message in messages:
    print(f"변수: {message.get('shortName', 'Unknown')}")
    print(f"  - 이름: {message.get('name', 'Unknown')}")
    print(f"  - 단위: {message.get('units', 'Unknown')}")
    print(f"  - 레벨 유형: {message.get('typeOfLevel', 'Unknown')}")
    print(f"  - 레벨: {message.get('level', 'Unknown')}")
    print(f"  - 단계: {message.get('step', 'Unknown')}")
    print("---")

# 각 레벨 유형별로 데이터셋 열기
level_types = set(m.get('typeOfLevel') for m in messages)

print("\n각 레벨 유형별 데이터 통계:")
for level_type in level_types:
    try:
        ds = xr.open_dataset(file_path, engine='cfgrib', 
                             backend_kwargs={'filter_by_keys': {'typeOfLevel': level_type}})
        print(f"\n레벨 유형: {level_type}")
        print(ds.variables)
        for var in ds.data_vars:
            if 'latitude' in ds[var].dims and 'longitude' in ds[var].dims:
                print(f"  {var}:")
                print(f"    최소값: {ds[var].min().values}")
                print(f"    최대값: {ds[var].max().values}")
                print(f"    평균값: {ds[var].mean().values}")
    except Exception as e:
        print(f"레벨 유형 {level_type}에 대한 처리 중 오류 발생: {e}")
