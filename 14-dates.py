Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import datetime
>>> #datetime.datetime, datetime.date, datetime.time
>>> n = datetime.datetime.today()
>>> type(n)
<class 'datetime.datetime'>
>>> print(n)
2019-08-10 01:54:29.273261
>>> n.day, n.month, n.year, n.hour , n.min, n.second, n.microsecond
(10, 8, 2019, 1, datetime.datetime(1, 1, 1, 0, 0), 29, 273261)
>>> n.hour
1
>>> n.min
datetime.datetime(1, 1, 1, 0, 0)
>>> n.minute
54
>>> n.day, n.month, n.year, n.hour , n.minute, n.second, n.microsecond
(10, 8, 2019, 1, 54, 29, 273261)
>>> n = datetime.date.today()
>>> type(n)
<class 'datetime.date'>
>>> n.day, n.month, n.year
(10, 8, 2019)
>>> print(n)
2019-08-10
>>> n = datetime.time()
>>> n
datetime.time(0, 0)
>>> print(n)
00:00:00
>>> 
>>> 
>>> datetime.datetime(year=2019, month=8, day=10)
datetime.datetime(2019, 8, 10, 0, 0)
>>> aug10 = datetime.datetime(year=2019, month=8, day=10)
>>> n = datetime.datetime.today()
>>> td = aug10 - n
>>> type(td)
<class 'datetime.timedelta'>
>>> td.days
-1
>>> td = n - aug10
>>> td.days
0
>>> n = datetime.datetime.today()
>>> aug11 = datetime.datetime(year=2019, month=8, day=11)
>>> td = aug11- n
>>> td.days
0
>>> td.total_seconds
<built-in method total_seconds of datetime.timedelta object at 0x000001F76A118330>
>>> td.total_seconds()
79178.023319
>>> td.seconds
79178
>>> td = datetime.timedelta(days=5)
>>> n
datetime.datetime(2019, 8, 10, 2, 0, 21, 976681)
>>> n + td
datetime.datetime(2019, 8, 15, 2, 0, 21, 976681)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> n.strftime('%d-%m-%y')
'10-08-19'
>>> n.strftime('%d-%M-%y')
'10-00-19'
>>> n.strftime('%d-%m-%yy')
'10-08-19y'
>>> n.strftime('%d-%m-%y')
'10-08-19'
>>> n.strftime('%d-%m-%Y')
'10-08-2019'
>>> s = '10-08-2019'
>>> dt = datetime.datetime.strptime(s, '%d-%m-%Y')
>>> dt
datetime.datetime(2019, 8, 10, 0, 0)
>>> print(dt)
2019-08-10 00:00:00
>>> dt + td
datetime.datetime(2019, 8, 15, 0, 0)
>>> (dt + td).strftime('%d-%m-%Y')
'15-08-2019'
>>> 
>>> 
>>> 
>>> 
>>> time.time()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    time.time()
NameError: name 'time' is not defined
>>> import time
>>> time.time()
1565383195.736964
>>> print(datetime.datetime.fromtimestamp(time.time()))
2019-08-10 02:10:47.463094
>>> 
