import pandas as pd

df_train = pd.read_csv('data/train.csv')
df_test = pd.read_csv('data/test.csv')
df = pd.concat([df_train, df_test])

# Removemos colunas irrelevantes e preenchemos nulos com 0
df = df.drop(['Unnamed: 0', 'id'], axis=1)
df['Arrival Delay in Minutes'] = df['Arrival Delay in Minutes'].fillna(0)

# Exportação
df.to_csv('data/aviation_cleaned.csv', index=False)