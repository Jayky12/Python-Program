import pandas as pd

df = pd.read_csv("emp.csv")

print(df.to_string())
print(df.describe())

sum_by_type = df.groupby('department')['salary'].sum()
# #แสดงผลลัพธ์
#print(sum_by_type)

# avg_by_type = df.groupby('department')['salary'].mean().round(2)
# max_by_type = df.groupby('department')['salary'].max()
# min_by_type = df.groupby('department')['salary'].min()
all_by_type = df.groupby('department')['salary'].agg(['sum','mean','max','min'])
all_by_type['mean'] = all_by_type['mean'].round(2)

#แสดงผลลัพธ์
# print(sum_by_type)

# sum_by_type_df = sum_by_type.reset_index()
# avg_by_type_df = avg_by_type.reset_index()
# max_by_type_df = max_by_type.reset_index()
# min_by_type_df = min_by_type.reset_index()
all_by_type_df = all_by_type.reset_index()

# print(sum_by_type_df)
# print(avg_by_type_df)
# print(max_by_type_df)
# print(min_by_type_df)
print(all_by_type_df)

