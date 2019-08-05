Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 100
>>> a= 10
>>> if a < 10:
	print("Single Digit")

	
>>> a < 10
False
>>> if a < 10:
	print("Single Digit")
else:
	print("May be double digit")

	
May be double digit
>>> if a < 10:
	print("Single Digit")
elif a < 100:
	print("Double Digit")
else:
	print("2+ digits")

	
Double Digit
>>> x = 3
>>> y = 10
>>> x > 2 and x < 6
True
>>> 2 < x < 6
True
>>> 2 < x < y < 20
True
>>> x> 2 or x < 6
True
>>> x < 2
False
>>> not x < 2
True
>>> li = ['India','USA','Russia', 'China']
>>> 'India' in li
True
>>> 'UK' not in li
True
>>> s = 'admin_sales'
>>> 'admin' in s
True
>>> 
