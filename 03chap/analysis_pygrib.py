import pygrib
import pandas as pd

def describe_grib(file_path):
    grbs = pygrib.open(file_path)
    
    # 기본 정보 수집
    messages = []
    for grb in grbs:
        messages.append({
            'name': grb.name,
            'level': grb.level,
            'dataDate': grb.dataDate,
            'dataTime': grb.dataTime,
            'validDate': grb.validDate,
            'validTime': grb.validTime,
            'units': grb.units
        })
    
    # DataFrame 생성
    df = pd.DataFrame(messages)
    
    print(f"GRIB2 파일 요약: {file_path}")
    print(f"총 메시지 수: {len(messages)}")
    print("\n변수 목록:")
    print(df['name'].value_counts())
    print("\n레벨 정보:")
    print(df['level'].value_counts())
    print("\n날짜 범위:")
    print(f"시작: {df['dataDate'].min()} {df['dataTime'].min()}")
    print(f"종료: {df['validDate'].max()} {df['validTime'].max()}")
    
    return df

# 사용 예
grib_summary = describe_grib("data/grib/gdas1.fnl0p25.2023072406.f00.grib2")