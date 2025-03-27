# csv - oddzielone znakiem podziału
import csv


"""
Kowalski,Jan,Kłodzko
Nowak,Zenon,Szczecin
Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
"""

fields = ['name', 'branch', 'year', 'cgpa']

row = ["Patryk", "test", "3", "0"]

dict1 = dict(zip(fields, row))
print(dict1)

filename = 'records.csv'
# newline ominięcie problemu pustej linii
with open(filename, 'w', newline ="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)


filename = 'records_dict.csv'
with open(filename, "w", newline="") as csv_fh:
    csvwriter = csv.DictWriter(csv_fh, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dict1)


products = [
    {"sku": 1, "exp_date": 'today', "price": 100},
    {"sku": 2, "exp_date": 'today', "price": 200},
    {"sku": 3, "exp_date": 'tomorr,ozzzzzzzz', "price": 500},
    {"sku": 4, "exp_date": 'today', "price": 50.00},
    {"sku": 5, "exp_date": 'today', "price": 99},
]
filename = 'records_products.csv'

fields_product = [key for key in products[0]]
print(fields_product)

with open(filename, 'w', newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)