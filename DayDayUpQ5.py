#三天打鱼两天晒网.py
dayup=1
dayfactor=0.01
for i in range(365):
    if i % 5 in [4,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("三天打鱼两天晒网的工作结果:{:.2f}".format(dayup))

