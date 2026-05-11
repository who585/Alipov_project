df = pd.read_csv('5 train.csv')

seasonal = df.groupby('season')[['casual', 'registered']].mean()

seasonal.plot(kind='bar')
plt.xlabel("Время года")
plt.ylabel("Среднее число поездок")
