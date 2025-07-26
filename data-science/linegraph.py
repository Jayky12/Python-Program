import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("graph.csv")

#pirnt(df.head())
#สร้งกราฟเส้น(line plot) โดยใช้คอลัมน์ 'x' 'y' ของ Dataframe
plt.plot(df['department'],df['mean'],label='Data',marker='o')
#เพิ่มชื่อกราฟและป้ายชื่อแกน
plt.title('Average Salary for Each Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')

#แสดงค่าบนกราฟ
for i in range(len(df)):
    plt.text(df['department'][i],df['mean'][i],f'{df["mean"][i]:.2f}',ha='center',va='bottom')

plt.legend()
plt.show()