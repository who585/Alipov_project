import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('5 train.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
weekend_mask = df['datetime'].dt.dayofweek >= 5
weekend_rides = df[weekend_mask]
hourly_rides = weekend_rides.groupby(weekend_rides['datetime'].dt.hour)['count'].sum()

max_hour = hourly_rides.idxmax()
max_rides = hourly_rides.max()

print(f" В выходные дни час пик — это {max_hour} часов.")
print(f" В это время совершается {max_rides} поездок")
