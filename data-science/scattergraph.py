import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('graph.csv')

plt.scatter(df['department'],df['mean'])

plt.title('Average Salary fot Each Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')

for i in range(len(df)):
    plt.text(df['department'][i],df['mean'][i],f'{df["mean"][i]:.2f}',ha='center',va='bottom')

plt.show()