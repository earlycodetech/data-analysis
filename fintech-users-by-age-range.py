import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_excel('fintech.xlsx',sheet_name='deposits')

#find number of user by age range, based on male gender
max_age = 80
current_age = 18
stepsize = 10

dict_data = {}

while current_age <= max_age:
    result = len(data[(data['Gender']=='male') & 
                  (data['Age'] >= current_age) & 
                  (data['Age'] <= current_age + stepsize)])
    
    this_key = str(current_age)+'-'+str(current_age+stepsize)
    dict_data[this_key] = result
    
    current_age += 11

x = list(dict_data.keys())
y = list(dict_data.values())

fig = plt.figure(figsize=(8,2),dpi=120)
axes = fig.add_axes([0,0.1,1,1])
axes.bar(x,y)
axes.set_title('Users by age range (Based on Males only)')
axes.set_xlabel('Age range')
axes.set_ylabel('Number of users')

plt.show()
