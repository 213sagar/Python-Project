# Write a python programe to display current date and time
import datetime
now=datetime.datetime.now()
print('current date and time is :')
print(now.strftime("%Y-%m-%d %H:%M:%S"))