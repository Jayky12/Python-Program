import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('graph.csv')

ax = sns.barplot(x='department',y='mean',data=df)
#เพิ่มชื่อกราฟ
plt.title('Average Salary fot Each Department')

for p in ax.patches:
    ax.text(p.get_x()+p.get_width() / 2,p.get_height(), f'{p.get_height():.2f}',ha='center',va='bottom',fontsize=10)

plt.show()