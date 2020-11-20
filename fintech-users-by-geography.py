import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_excel('fintech.xlsx',sheet_name='deposits')

#find numbers of users by Geography

rural = len(data[data['Geography']=='rural'])
urban = len(data[data['Geography']=='urban'])

print(rural)
print(urban)

#plot a bar to represent data
plt_bar = {'Rural':rural,'Urban':urban}
x = list(plt_bar.keys())
y = list(plt_bar.values())

fig = plt.figure(figsize=(1,2),dpi=120)
axes = fig.add_axes([0.1,0.1,1,1])
axes.bar(x,y)
axes.set_title('Number of users by Geography')
axes.set_xlabel('Geography')
axes.set_ylabel('Number of users')

plt.show()
