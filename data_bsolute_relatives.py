import pandas as pd
data= {'jobs': ['DBA','DEV', 'NetArq' ],
       'new_jersey':[97350, 82080,112840],
       'florida': [77140, 71540, 622310]}
dataset = pd.DataFrame(data)
print(dataset)
total_nj = dataset['new_jersey'].sum()
total_fl = dataset['florida'].sum()
dataset['percent_fl'] = dataset['florida']/ total_fl * 100
dataset['percent_nj'] = dataset['']/ total_fl * 100

