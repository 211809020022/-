#DayDayUpQ2.py
dayfactor=0.01
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("dayup={:.2f},daydown={:.2f}".format(dayup,daydown))
