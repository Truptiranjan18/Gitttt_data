from datetime import date, datetime

current_date=date.today().strftime('%d-%m-%Y')
current_time=datetime.now().strftime("%H:%M:%S")
print(current_date,current_time)