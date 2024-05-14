'''Create two base classes named clock and calendar. Based on these two class define
a class calendarclock, which inherits from both the classes which displays month
details, date and time.'''

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def display_time(self):
        print(f"Time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")


class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def display_date(self):
        print(f"Date: {self.day:02d}-{self.month:02d}-{self.year}")


class CalendarClock(Clock, Calendar):
    def __init__(self, day, month, year, hours, minutes, seconds):
        Clock.__init__(self, hours, minutes, seconds)
        Calendar.__init__(self, day, month, year)
    
    def display(self):
        self.display_date()
        self.display_time()

# Example usage:
if __name__ == "__main__":
    my_clock = CalendarClock(25, 4, 2024, 12, 30, 45)
    my_clock.display()
