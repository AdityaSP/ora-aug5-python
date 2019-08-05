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
>>> 
>>> li
['India', 'USA', 'Russia', 'China']
>>> count =0
>>> while count < len(li):
	print(li[count].upper())
	count += 1

	
INDIA
USA
RUSSIA
CHINA
>>> while count < len(li):
	print(li[count].upper())
	count += 1

	
>>> count =0
>>> while count < len(li):
	print(li[count].upper())
	count += 1

	
INDIA
USA
RUSSIA
CHINA
>>> li
['India', 'USA', 'Russia', 'China']
>>> for country in li:
	print(country.upper())

	
INDIA
USA
RUSSIA
CHINA
>>> range(5)
range(0, 5)
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> li = ['Hope', 'lives', 'ON', 'Smile', 'to', 'let', 'you', 'Smile', 'hope']
>>> for i in range(li.count('Smile')):
	li.remove('Smile')

	
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope']
>>> 
>>> 
>>> import random
>>> random.randint(0,100)
27
>>> random.randint(0,100)
36
>>> 20 --> Low, 50 --> High, 40--> high, 30--> low
