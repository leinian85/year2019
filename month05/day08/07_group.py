import numpy as np
import pandas as pd
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print("#",' 无分组')
print(df)
print("#",' 按年份排序')
print(df.sort_index(by=['Year']))
print("#",' 按年份分组')
print(df.groupby(by='Year').get_group(2014))

df_groupd = df.groupby(by='Year')
print("#",' 按年份分组求最得分的平均值,最小值,最大值,标准差')
print(df_groupd['Points'].agg([np.mean,np.min,np.max,np.std]))

print(df_groupd['Points'].agg([np.mean,np.min,np.max,np.std]).values)
# for one in df.groupby('Year')['Points'].agg([np.mean,np.min,np.max,np.std]):
#     print(one)

# for year,group in df.groupby(by='Year'):
#     print(year,group)
