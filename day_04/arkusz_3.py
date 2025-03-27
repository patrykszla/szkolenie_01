import pandas as pd
import numpy as np

technologies = ["Spark", "Pandas", "Python", "PHP"]
fee = [25000, 20000, 15000, 18000, 22200]

duration = ['50 days', '35 days', np.nan, '30 Days']

discount = [2000, 1000, 800, 500, 500]


columns = ['Courses', 'Fee', 'Durations', 'Discount']

df = pd.DataFrame(list(zip(technologies, fee, duration, discount)),
                  columns=columns)

print(df)


df.to_excel('courses.xlsx')
df.to_excel('courses_no_index.xlsx', index=False)


excel_data = pd.read_excel('courses_no_index.xlsx')
print(excel_data)

data = pd.DataFrame(excel_data)