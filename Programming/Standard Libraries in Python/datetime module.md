# datetime module

datetime module allows to work with Date, Time and Timedelta Time zones.

### date()

- date() method gives us the date in YYYY-MM-DD format
- While specifying month in date() method don’t use trailing zero before it like 04,09,etc.

```python
import datetime as dt
date=dt.date(2001,4,20) 
print(date)
```

### today() class

- **today()** class gives us the todays date object.
- today() object contains year, month, day, etc. attributes.
- today() object have different methods like **weekday()**, **isoweekday(), isocalender(),** etc.
- In case of normal weekday starts with Monday-0 and ends with sunday-6.
- In case of iso weekday starts with Monday-1 and ends with sunday-7.

```python
todayDate=dt.date.today() # gives us the today date
print(todayDate)
# atrributes
print(todayDate.year)     # prints only the year
print(todayDate.month)    # prints only the month
print(todayDate.day)    # prints only the day
# methods
print(todayDate.weekday())      # gives us the weekday value   In, weekday starts withnMonday-0 and ends with sunday-6
print(todayDate.isoweekday())   # gives us the isoweekday value In, isoweekday starts withnMonday-1 and ends with sunday-7
print(todayDate.isocalendar())  # gives us the output as datetime.IsoCalendarDate(year=2023, week=33, weekday=5) and it consists of how many weeks completed and isoweekday of today date
```

### deltatime()

- **deltatime()** is used to add/subtract days, hours, minutes, seconds, microseconds, milliseconds and weeks to any **date()** and **datetime()** object.
- Gives us the object that contains days, hours, minutes, seconds, microseconds, milliseconds and weeks attributes.
- **Syntax:**

```python
datetime.deltatime(days: float = ..., seconds: float = ..., microseconds: float = ..., milliseconds: float = ..., minutes: float = ..., hours: float = ..., weeks: float = ...) -> timedelta
```

- Upon adding date and deltatime ,the result is date and adding date and date gives us deltatime.
    - date=date + deltatime
    - deltatime=date1 - date2  ,this gives us timedelta object with no. of days and have method called **total_seconds()** to get no. of seconds.

```python
delta=dt.timedelta
N=7  # No. of weeks
timedeltaforAfterNweeks=dt.timedelta(weeks=N)     #creating a timedelta object with N weeks
dateAfterNweeks=timedeltaforAfterNweeks+todayDate             
print(dateAfterNweeks)                            #gives us date object of after N weeks

myBirthDayDate=dt.date(2024,4,20)     #creating a date object
diff=myBirthDayDate-todayDate         #gives us timedelta object
print(f"Total No of Days for next birthday: {diff.days}")
print(f"Total No of seconds for next birthday: {diff.total_seconds()}")
```

### time()

- Creates a time object with specified inputs.
- The time object have attributes like hour, minute, etc.. and we can access them easily.

```python
timeObj=dt.time(hour=13,minute=34,second=45,microsecond=2345) # creates a time object with specified inputs.
print(timeObj) #prints the time object and we can access each attributes also like hour,minute,etc..
```

## datetime.datetime()

- datetime class have combination of date and time & today() method return the current date and time.
- The datetime object created also have date() and time() methods

```python
dateTime=dt.datetime.today()  # datetime class have combination of date and time & today() method return the current date and time.
print(dateTime)               # prints the current date and time
print(dateTime.date())        # prints only date
print(dateTime.time())        # prints only time
```

## Add time to datetime using timedelta() method

```python
# below code is to add some hours to current time
N=12  # no. of hours
timedelta=dt.timedelta(hours=N)
timeAfterNhours=timedelta+dateTime
print(timeAfterNhours)
```

### today() VS now() VS utcnow()

- **today()** and **now()** gives us naive local time in which doesn’t have time zone.
- **utcnow()** gives us universal time coordinated with time zone UTC .
- **today()** and **now()** have tzinfo and tz arguments which is set to **None**.
- But this can updated with different time zone ****and it only works with utc.

```python
dateTime=dt.datetime.today()  # datetime class have combination of date and time & today() method return the current date and time.
print(dateTime)               # prints the current date and time
print(dateTime.date())        # prints only date
print(dateTime.time())        # prints only time
dateTimeUsingNow=dt.datetime.now()           # today() and now() methods gives us same time.
dateTimeUsingUTCNow=dt.datetime.utcnow()     # this follows UTC time zone
print(dateTimeUsingNow)
print(dateTimeUsingUTCNow)
```

# pytz library

- **[pytz](https://pypi.org/project/pytz/)** is library that can be used in python 2.4 or higher and it is added to python standard library in python 3.9 version.
- It provides us different time zones of
- The preferred way of dealing with times is to always work in UTC, converting to local time only when generating output to be read by humans.

### Converting Asia/Kolkata time to Europe/Amsterdam using pytz module

Follow the below Steps:

- Take out the local machine time without time zone using **now()** method.
- Pass local machine time to **localize()** method and call this method local time zone. By doing so it will time zone.
- Then, call **astimezone()** method with localized time then pass time zone of your desired country i.e.; Europe/Amsterdam.

```python
#converting Asia/Kolkata time to Europe/Amsterdam using pytz module
print("converting Asia/Kolkata time to Europe/Amsterdam")

fmt="%Y %m %d %H:%M %S %Z %z"
dt_kol=dt.datetime.now()
print(f"Asia/Kolkata time without timezone: {dt_kol}")
kol_tz=pytz.timezone("Asia/Kolkata")
local_dt=kol_tz.localize(dt_kol)
print(f"Asia/Kolkata time with timezone: {local_dt}")
amster_dt=local_dt.astimezone(pytz.timezone("Europe/Amsterdam"))
print(f"Europe/Amsterdam time with timezone:  {amster_dt.strftime(fmt)}")

print(f"Europe/Amsterdam time with timezone using pytz: {dt.datetime.now(pytz.timezone('Europe/Amsterdam'))}")
```

### Format codes for strftime() and stptime()

Check out in official document- [**format codes**](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

### strftime()

- Used to convert datetime object to string
- Takes one argument i.e.; formatted string

```python
#strftime - used to convert datetime object to string
fmt="%B %d, %Y"
str_date=amster_dt.strftime(fmt)
print(f"Europe/Amsterdam time with timezone:  {str_date}")
```

### strptime()

- Used to convert from string to date time object
- Takes two arguments one is datetime string and other is formatted string

```python
#strptime - used to convert string to datetime object
print(f"Europe/Amsterdam time with timezone:  {dt.datetime.strptime(str_date,fmt)}")
```

# Some other python libraries to manage date and time

- a[**rrow**](https://arrow.readthedocs.io/en/latest/) - arrow also includes dateutil
- [**dateutil**](https://dateutil.readthedocs.io/en/stable/)