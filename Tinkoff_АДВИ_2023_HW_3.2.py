import pandas as pd
import numpy as np
import math
import random

# 0
random.seed('АДВИ_2023')
N = 1000

# 1
index_column = [i for i in range(1, N + 1)]
random.shuffle(index_column)

# 2
groups = ["группа_1", "группа_2", "группа_3", "группа_4", "группа_5"]
groups_column = [random.choice(groups) for i in range(N)]

# 3
uniform_column = [random.randint(50, 100) for i in range(N)]

# 4
gauss_1_column = [random.gauss(0, math.sqrt(1)) for i in range(N)]
gauss_2_column = [random.gauss(0, math.sqrt(144)) for i in range(N)]
gauss_3_column = [random.gauss(50, math.sqrt(81)) for i in range(N)]

# 5
data = {
    'index' : index_column,
    'groups' : groups_column,
    'uniform' : uniform_column,
    'gauss_1' : gauss_1_column,
    'gauss_2' : gauss_2_column,
    'gauss_3' : gauss_3_column
    }
df = pd.DataFrame(data)
# print(df)

# 6
df.loc[df.index % 121 == 0, 'gauss_1'] = None
df.loc[df['gauss_2'].apply(lambda x: abs(x) % 1 > 0.95), 'gauss_2'] = None

# 7
df.loc[df['gauss_2'].isnull(), 'gauss_2'] = df['gauss_2'].mean()
df.dropna(subset=['gauss_1'], inplace=True)

# Выполнение заданий

# 1
# print(df)

# 2
# print(round(df.mean(), 2))
# print('-' * 20)
# print(round(df.std(), 2))

# 3
# print(df['groups'].value_counts())

# 4
# print(df)

# 5
# percentile = np.percentile(df.uniform, 90)
# print(percentile)

# 6
# gr = df.groupby('groups')['gauss_3'].median()
# print(gr)

# 7
min_ = df.groupby('groups')['uniform'].median()
print(min_)
