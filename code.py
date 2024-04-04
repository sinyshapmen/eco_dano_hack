import pandas as pd

df = pd.read_csv('final.csv')
df.drop(columns=['наличие_менеджера_по_окр_среде', 'наличие_выбросов_CO2'], inplace=True)
df['отслеживание_выбросов_CO2'].fillna('Нет', inplace=True)
df = df.replace({'Не знаю': 'Нет', 'Не применимо': 'Да'})
df.replace({'Нет': 0, 'Да': 1}, inplace=True)

df[criteria] = df[criteria].replace('Не применимо', np.nan)
df['Сумма критериев'] = df[criteria].sum(axis=1)
total_columns = len(criteria) - df[criteria].isna().sum(axis=1)
df['Общее количество критериев'] = total_columns
df['Сумма критериев'] = df['Сумма критериев'].astype(int)