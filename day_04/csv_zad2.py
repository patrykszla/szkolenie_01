import csv

filename = "records.csv"
filename = "records_products.csv"

fields = []
rows = []

with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    print(dialect.delimiter)
    csvreader = csv.reader(f, delimiter=dialect.delimiter)

    print(csvreader)
    fields = next(csvreader) # porabnie jednego elementu iteratora

    for row in csvreader:
        print(row)
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)