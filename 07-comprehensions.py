Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> # list
>>> li = [2,3,4]
>>> newli = []
>>> for i in li:
	newli.append(i*i)

	
>>> newli
[4, 9, 16]
>>> list(map(lambda x : x* x, li))
[4, 9, 16]
>>> #[<expression> <for statement>]
>>> [ i*i for i in li]
[4, 9, 16]
>>> s = '12,34,56'.split(',')
>>> s
['12', '34', '56']
>>> sum(map(int,s))
102
>>> sum([int(i) for i in s])
102
>>> 
>>> 
>>> 
>>> li = [23,34,56,67]
>>> # sum of squares of even numbers
>>> sum(map(lambda x :x *x, filter(lambda x : x %2 ==0, li)))
4292
>>> 34*34+56*56
4292
>>> #[<expression> <for statement> <if gate>]
>>> 
>>> 
>>> [ i*i for i in li if i%2 ==0]
[1156, 3136]
>>> sum([ i*i for i in li if i%2 ==0])
4292
>>> li = ['how are you', 'what are you', 'where are you']
>>> [ i.split() for i in li ]
[['how', 'are', 'you'], ['what', 'are', 'you'], ['where', 'are', 'you']]
>>> [ len(i.split()) for i in li ]
[3, 3, 3]
>>> sum([ len(i.split()) for i in li ])
9
>>> 
>>> 
>>> low = []
>>> for line in li:
	for word in line.split():
		low.append(word)

		
>>> low
['how', 'are', 'you', 'what', 'are', 'you', 'where', 'are', 'you']
>>> [ word for line in li for word in line.split()]
['how', 'are', 'you', 'what', 'are', 'you', 'where', 'are', 'you']
>>> 
