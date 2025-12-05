from datetime import datetime

years = input("your birthyear: ")
month = input("your birthmonth: ")
day = input("your birthday: ")

current_date = datetime.today()
born = datetime(int(years), int(month), int(day))
difference = current_date - born
print(difference.days // 365)