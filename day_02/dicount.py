from datetime import datetime, date, timedelta
from time import strptime

today = date.today()
print(today)
print(type(today))

time = datetime.now()
print("Aktualny czas ", time)
print(type(time))

print(time.year)
print(today.day)

tomorrow = today + timedelta(1)
print(tomorrow)

formated_data = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data:", formated_data)

formated_time = datetime.now().strftime("%H:%M")
print("Sformatowany czas:", formated_time)
print(type(formated_time))

formated_usa_time = datetime.now().strftime("%I:%M %p")
print("Czas USA:", formated_usa_time)
print("Czas USA:", formated_usa_time.removeprefix("0"))

date_datetime = datetime.now().strptime("25/03/2025", "%d/%m/%Y")
print(date_datetime)

products = [
    {"sku": 1, "exp_date": today, "price": 100},
    {"sku": 2, "exp_date": today, "price": 200},
    {"sku": 3, "exp_date": tomorrow, "price": 500},
    {"sku": 4, "exp_date": today, "price": 50.00},
    {"sku": 5, "exp_date": today, "price": 99},
]

# print(products)
print("-------- PRODUKTY ---------")
new_products = []
for product in products:
    print(product)
    print(product['exp_date'])
    if product['exp_date'] != today:
        print('DZISIEJSZA!!')
        continue  # wraca na początek pętli a pass przechodzi dalej!!
    print("zmiana ceny")
    product['price'] *= 0.8
    print(f"""Price for sku {product['sku']}
is now {product['price']}""")

# print(products)