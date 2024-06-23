from datetime import timedelta

# create the time delta object for 100 days, 10 hours, and 13 minutes
delta = timedelta(days=100, hours=10, minutes=13)

# Will print the timedelta object
print(delta)

# print only the day component of the timedelta object
print(delta.days)

# Redefines components of the timedelta object and then prints them
days = delta.days
seconds = delta.seconds
microseconds = delta.microseconds
print(days, seconds, microseconds)




