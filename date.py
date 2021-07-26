from datetime import datetime, timedelta, date
today = datetime.today()
print(today)

ID = "912285835083"

year = int(ID[0:2])
month = int(ID[2:4])
day = int(ID[4:6])

dob = date(int(year), int(month), int(day))
age_cal = (date.today() - dob) // timedelta(days=365.2425)
print(age_cal)

