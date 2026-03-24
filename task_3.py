df = pd.read_csv('5 train.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
hourly_rides = df.groupby(weekend_rides['datetime'].dt.month)[['temp','count']].mean()
hourly_rides.to_csv("Средняя температура и число поездок по месяцам.csv", sep=";")


