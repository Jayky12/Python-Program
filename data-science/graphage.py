import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('age.csv')

df_melted = pd.melt(df,id_vars=['age'],value_vars=['max','mean','min'],var_name='Salary Type',value_name='Salary')

ax = sns.barplot(x='age',y='Salary',hue='Salary Type',data=df_melted)

plt.title('Salary(Max, Mean, Min) for Each Age')

for p in ax.patches:
    ax.text(p.get_x()+p.get_width() / 2,p.get_height(), f'{p.get_height():.2f}',ha='center',va='bottom',fontsize=10)

plt.show()