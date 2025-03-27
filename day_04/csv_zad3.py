import pandas

data = pandas.read_csv('records.csv')
data = pandas.read_csv('records_products.csv', delimiter=";")

print(data)
print(data.values)
print(data.columns)
print(data.items)