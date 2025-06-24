from datetime import date
import calendar

class Date:
    def today():
        return date.today().isoformat()

    def next_month():
        today = date.today()
        year = today.year
        month = today.month

        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

        day = min(today.day, calendar.monthrange(year, month)[1])
        next_month_date = date(year, month, day)

        return next_month_date.isoformat()
