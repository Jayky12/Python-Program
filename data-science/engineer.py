import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('emp.csv')

engineer_data =df[df['position'] ==  'Engineer']

plt.figure(figsize=(10,6))
bars = plt.bar(engineer_data['emp_code'], engineer_data['salary'], color='skyblue')

plt.xlabel('Emp_code')
plt.ylabel('Salary')
plt.title('Salary of Employee with Position Engineer')
plt.xticks(rotation=45,ha='right')

for bar in bars :
    yval = bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2,yval,round(yval,2),ha='center',va='bottom',fontsize=10)

plt.tight_layout()

plt.show()