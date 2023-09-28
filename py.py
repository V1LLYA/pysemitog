import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.DataFrame()

unique_values = data['whoAmI'].unique()

for value in unique_values:
    one_hot_data[f'{value}_onehot'] = (data['whoAmI'] == value).astype(int)

print(one_hot_data.head())
