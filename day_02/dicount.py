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

date_datetime = datetime.now().strptime("25/03/2025", "%d/%m/%Y" )
print(date_datetime)