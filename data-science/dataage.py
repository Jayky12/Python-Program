import pandas as pd

df = pd.read_csv("emp.csv")

print(df.to_string())
print(df.describe())

all_by_type = df.groupby('age')['salary'].agg(['sum','mean','max','min'])
all_by_type['mean'] = all_by_type['mean'].round(2)
all_by_type_df = all_by_type.reset_index()


df=pd.DataFrame(all_by_type_df)
df.to_csv('age.csv',index=False,encoding='utf-8-sig')
print(all_by_type_df)