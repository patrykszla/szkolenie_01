import pandas as pd

excel_data = pd.read_excel('sales.xlsx')
print(excel_data)

data = pd.DataFrame(excel_data)

print(data.values)
print(data.columns)
print(data.items)


print(data[data['Amount'] > 40000])