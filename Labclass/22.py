from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def day_message(day):
    if day == Weekday.MONDAY:
        print("Start of the workweek!")
    elif day == Weekday.TUESDAY:
        print("Keep going, it's Tuesday!")
    elif day == Weekday.WEDNESDAY:
        print("Midweek already!")
    elif day == Weekday.THURSDAY:
        print("Almost there, it's Thursday!")
    elif day == Weekday.FRIDAY:
        print("Friday vibes are here!")
    elif day == Weekday.SATURDAY:
        print("Enjoy your Saturday!")
    elif day == Weekday.SUNDAY:
        print("Relax, it's Sunday!")
    else:
        print("Invalid day!")


day_message(Weekday.FRIDAY)
