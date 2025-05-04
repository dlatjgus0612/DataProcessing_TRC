import numpy as np

# degrees and m/s
wind_direction_degrees = 135
wind_speed_mps = 2.7

# degree to radian
theta_rad = np.deg2rad(270 - wind_direction_degrees)

# U : East Component 계산
u_component = wind_speed_mps * np.cos(theta_rad)
# V : West Component 계산
v_component = wind_speed_mps * np.sin(theta_rad)

print("U component (East) : ", u_component)
print("V component (West) : ", v_component)

# wind_direction = 풍향 (각도)------------------------
def get_east_component(wind_direction, wind_speed_mps):
    theta_rad = np.deg2rad(270 - wind_direction)
    return wind_speed_mps * np.cos(theta_rad)
def get_west_component(wind_direction, wind_speed_mps):
    theta_rad = np.deg2rad(270 - wind_direction)
    return wind_speed_mps * np.sin(theta_rad)

wind_direction = 135
print("U def : East : ", get_east_component(wind_direction, wind_speed_mps))
print("V def : West : ", get_west_component(wind_direction, wind_speed_mps))