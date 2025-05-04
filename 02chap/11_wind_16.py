import math

def get_wind_direction_16(wind_direction):
    # 360도를 16등분하여 16방위로 나누기
    index = int((wind_direction + 11.25) // 22.5) % 16
    # math.floor((wind_direction + 11.25)/22.5) 해도 되지만 그냥 계산 후 int 하는 것 과 값이 같다. 
    return directions[index]

# Define 16 directions
directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", 
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]

wind_direction = float(input("풍향을 입력하세요 : "))
print("16방위 값 : ", get_wind_direction_16(wind_direction))
