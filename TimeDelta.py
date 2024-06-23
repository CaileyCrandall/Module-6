from datetime import datetime, timedelta

# subtract 60 seconds from current time
print(datetime.now() - timedelta(seconds=60))

# add two years to current date
print(datetime.now() + timedelta(days=720))
