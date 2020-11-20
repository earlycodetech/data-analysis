import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_excel('fintech.xlsx',sheet_name='deposits')

#find number of users by gender
male = len(data[data['Gender']=='male'])
female = len(data[data['Gender']=='female'])

dict_gender = {'Male':male,'Female':female}
labels_ = list(dict_gender.keys())
values = list(dict_gender.values())

fig = plt.figure(figsize=(3,3),dpi=120)
axes = fig.add_axes([0.1,0.1,1,1])
axes.pie(values,startangle=90,shadow=True,autopct='%1.0f%%',
         labels=labels_,explode=[0.1,0])

axes.set_title('Users Based on Gender')

plt.show()
