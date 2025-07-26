import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('graph.csv')

plt.scatter(df['department'],df['mean'],color='blue',label='Mean')
plt.scatter(df['department'],df['max'],color='green',label='Max')
plt.scatter(df['department'],df['min'],color='red',label='Min')

plt.title('Average (Max, Mean, Min) fot Each Department')
plt.xlabel('Department')
plt.ylabel('Salary')

for i in range(len(df)):
    plt.text(df['department'][i],df['mean'][i],f'{df["mean"][i]:.2f}',ha='center',va='bottom',color='blue')
    plt.text(df['department'][i],df['max'][i],f'{df["max"][i]:.2f}',ha='center',va='bottom',color='green')
    plt.text(df['department'][i],df['min'][i],f'{df["min"][i]:.2f}',ha='center',va='bottom',color='red')

plt.show()