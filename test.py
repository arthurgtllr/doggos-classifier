import pandas as pd
import constants

df = pd.read_csv(constants.RAW_DATA_PATH + '/raw_data.csv')

print(df['class'].value_counts())