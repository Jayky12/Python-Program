import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('graph.csv')
#สร้าง data frame ใหม่
df_melted = pd.melt(df,id_vars=['department'],value_vars=['max','mean','min'],var_name='Salary Type',value_name='Salary')
#สร้งกราฟ 
ax = sns.barplot(x='department',y='Salary',hue='Salary Type',data=df_melted)

#เพิ่มชื่อกราฟ
plt.title('Salary(Max, Mean, Min) fot Each Department')

for p in ax.patches:
    ax.text(p.get_x()+p.get_width() / 2,p.get_height(), f'{p.get_height():.2f}',ha='center',va='bottom',fontsize=10)

plt.show()