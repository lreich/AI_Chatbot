import pandas as pd
import matplotlib
import numpy as np
pd.__version__

pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

# california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
# print(california_housing_dataframe.describe())
# print(california_housing_dataframe.head())
# california_housing_dataframe.hist('housing_median_age')
print(np.log(population))
