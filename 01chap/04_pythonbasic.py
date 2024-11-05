'''
degree, minute, second 로 된 위치정보를 실수형 도 decimal degree
decimal degree = degree + minute/60 + second/3600
'''
print("--------1. 위도 경도 변환 문제--------")

lat_deg = int(input("변환 하려는 위도 degree값은 ? "))
lat_min = int(input("위도의 miunte 값은 ? "))
lat_sec = int(input("위도의 second 값은 ? "))
# lat_deg, lat_min, lat_sec = map(int, input("위도 degree, min, sec 띄어쓰기로 구분하여 입력 : ").split())

long_deg = int(input("변환 하려는 위도 degree값은 ? "))
long_min = int(input("위도의 miunte 값은 ? "))
long_sec = int(input("위도의 second 값은 ? "))
# long_deg, long_min, long_sec = map(int, input("경도 degree, min, sec 띄어쓰기로 구분하여 입력 : ").split())

decimal_lat = lat_deg + lat_min/60 + lat_sec/3600
decimal_long = long_deg + long_min/60 + long_sec/3600

print(f"latitude = {decimal_lat:.5f}")
print(f"longitude = {decimal_long:.5f}")

'''
degree = int(decimal_deg)
minute = int((decimal_deg - degree) * 60)
second = ((decimal_deg - degree) * 60 - minute) * 60
'''
print("--------2. 실수형으로 받아보자--------")
decimal_lat = float(input("변환하려는 latitude (decimal degree 입력) : "))
decimal_long = float(input("변환하려는 longitude (decimal degree 입력) : "))

# define function 
def convert_decimal_to(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes_decimal = (decimal_degrees - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = (minutes_decimal - minutes) * 60

    return degrees, minutes, seconds

lat_deg, lat_min, lat_sec = convert_decimal_to(decimal_lat)
long_deg, long_min, long_sec = convert_decimal_to(decimal_long)

print(f"latitude is : {lat_deg}-{lat_min}-{lat_sec:.2f}")
print(f"longitude is : {long_deg}-{long_min}-{long_sec:.2f}")