# Date (15) 

## Importing the datetime function from datetime library
from datetime import datetime

## Importing the timedelta function from datetime library
from datetime import timedelta

## Alternative import of both datetime and timedelta
## from datetime import datetime, timedelta

## Showing the current date and time
right_now = datetime.now()
print('Today:')
print(right_now)

## Functions with dates
### Showing the last week
one_week = timedelta(weeks=1)
last_week = right_now - one_week
print('Last week:')
print(last_week)

## Turning a string into a date
arbitrary_date = input('Please, enter a date (dd/mm/yyyy): ')
print(arbitrary_date)
print(type(arbitrary_date))

arbitrary_date = datetime.strptime(arbitrary_date, '%d/%m/%Y')
print(arbitrary_date)
print(type(arbitrary_date))

## Using date functions on the input
one_day = timedelta(days=1)
arbitrary_yesterday = arbitrary_date - one_day
print(arbitrary_yesterday)

## Catching parts of a date
arbitrary_day = arbitrary_date.day
print('Day: ', arbitrary_day)
arbitrary_month = arbitrary_date.month
print('Month: ', arbitrary_month)
arbitrary_year = arbitrary_date.year
print('Year: ', arbitrary_year)
