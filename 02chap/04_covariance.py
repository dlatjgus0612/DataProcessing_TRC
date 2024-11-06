import numpy as np
import pandas as pd 

obs_wind_speed = [2, 4, 7, 8, 9, 12, 18, 13, 12, 19, 8, 9]
mod_wind_speed = [3, 4, 6, 10, 15, 11, 12, 24, 20, 24, 9, 8]

data = {'Observed' : obs_wind_speed, 'Model' : mod_wind_speed}
df = pd.DataFrame(data)

# Cacluate covariance using numpy
cov_matrix_np = np.cov(obs_wind_speed, mod_wind_speed, ddof=1)
covariance_np = cov_matrix_np[0,1]

# Cacluate covariance using Pandas
cov_matrix_pd = df.cov()
covariance_pd = cov_matrix_pd.loc['Observed', 'Model']

print("Covariance using numpy: {:.2f}".format(covariance_np))
print("Covariance using pandas: {:.2f}".format(covariance_pd))