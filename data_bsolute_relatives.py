import pandas as pd
data= {'jobs': ['DBA','DEV', 'NetArq' ],
       'new_jersey':[97350, 82080,112840],
       'florida': [77140, 71540, 62310]}
dataset = pd.DataFrame(data)

total_nj = dataset['new_jersey'].sum()
total_fl = dataset['florida'].sum()
dataset['percent_fl'] = dataset['florida']/ total_fl * 100
dataset['percent_nj'] = dataset['new_jersey']/ total_nj * 100
dataset['percent_nj'] =dataset['percent_nj'].astype(int)
dataset['percent_fl'] =dataset['percent_fl'].astype(int)
print(dataset)
