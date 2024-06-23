from datetime import datetime

time_now = datetime.now()


def growth_tracker():
    print("Let's track your growth. How tall are you in feet & inches?")
    feet = int(input("How many feet? "))
    inches = int(input("How many inches? "))
    print("At " + str(time_now) + " you are " + str(feet) + " feet, " + str(inches) + " inches.")


growth_tracker()
