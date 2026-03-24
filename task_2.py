df = pd.read_csv('5 train.csv')

hot = df[df['count'] > 500]

seasons = hot.groupby('season').size()

top_season = seasons.idxmax()
top_count = seasons.max()

print(f'Всего наблюдений  > 500: {len(hot)}')
print(f' СЕЗОН: {top_season} ')
print(f'поездок: {top_count}')

