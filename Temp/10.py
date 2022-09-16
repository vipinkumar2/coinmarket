# Simple Python program to compare dates

# importing datetime module
import datetime

# date in yyyy/mm/dd format
d1 = datetime.datetime.now()
d2 = datetime.datetime(2003, 6, 1)
print(d1+d2)
# Comparing the dates will return
# either True or False
print("d1 is greater than d2 : ", d1 > d2)
print("d1 is less than d2 : ", d1 < d2)
print("d1 is not equal to d2 : ", d1 != d2)
print(type(d1)=='datetime.datetime')
print((d1-d2).total_seconds())

a = [0]
print(len(a) > 0)


# https://coinmarketcap.com/currencies/xana/
