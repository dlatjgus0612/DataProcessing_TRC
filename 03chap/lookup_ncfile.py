from netCDF4 import Dataset

def summarize_nc_file(file_path):
    # NetCDF 파일 열기
    with Dataset(file_path, 'r') as dataset:
        # 파일에 포함된 변수 목록
        print("--------------------------------------")
        print(f"Variables in {file_path}:")
        for var_name in dataset.variables:
            print(f" - {var_name}: {dataset.variables[var_name].shape}")
        
        # 파일에 포함된 속성 (메타데이터) 출력
        print("\nGlobal attributes:")
        for attr_name in dataset.ncattrs():
            print(f"\r - {attr_name}: {getattr(dataset, attr_name)}")

        
        # 파일의 차원 정보
        print("\nDimensions:")
        for dim_name, dim in dataset.dimensions.items():
            print(f" - {dim_name}: {len(dim)}")

# 예시 파일 경로
file1, file2 = 'data/sst.day.mean.nc', 'data/icec.day.mean.nc'

summarize_nc_file(file1)
summarize_nc_file(file2)
