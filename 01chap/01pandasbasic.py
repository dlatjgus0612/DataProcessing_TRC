import pandas as pd
from collections import OrderedDict

# 1. pandas를 통한 파일 읽기 
def read_pandas():
    track_data = "data/track_XY.txt"
    df = pd.read_table(track_data,
                       sep="\s+",                                      # 구분자
                       encoding="euc-kr",                              # 인코딩 타입
                       names=['longitude', 'latitude'],                # 컬럼명
                       dtype={'longitude': float, 'latitude': float})  # 컬럼 데이터 타입

    # 전체 평균, 최대, 최소 계산
    summary = df.agg(['mean', 'max', 'min'])

    # 결과 출력
    print("Summary Statistics:")
    print(summary)
    
 

# 2. pandas를 통한 파일 쓰기 
def write_pandas():
    friend_ordered_dict = OrderedDict([
        ('name',['John','Peter','pi']),
        ('age',[25,30,40]),
        ('weight',[75.3, 64.5, 3.141592653]),
        ('job',['student','연구원','교수']),
    ])
    
    df = pd.DataFrame.from_dict(friend_ordered_dict)
    df.to_csv("data/save1.csv", encoding="utf-8", index=False, header=True)
    # 인코딩을 UTF-8로 변경하고 index (0,1,2) 제거 

# 메인 실행
read_pandas()  
write_pandas()   
