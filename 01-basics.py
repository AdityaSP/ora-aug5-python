Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> print('Hello World!')
Hello World!
>>> print('''Hello World!''')
Hello World!
>>> print("""Hello World!""")
Hello World!
>>> print("""Hello World
It's a "good" Monday""")
Hello World
It's a "good" Monday
>>> # """ --> used for multi line strings
>>> # built ins
>>> a = 10
>>> b = 23.5
>>> c = 'Hello'
>>> d = True
>>> # no declartion
>>> # Dynamic programming --> no dataype mentioned
>>> 
>>> # strongly typed programming langauge
>>> type(a)
<class 'int'>
>>> type(b), type(c), type(d)
(<class 'float'>, <class 'str'>, <class 'bool'>)
>>> print(a)
10
>>> print(a,b,c,d)
10 23.5 Hello True
>>> a
10
>>> a,b,c,d
(10, 23.5, 'Hello', True)
>>> 
>>> a = c
>>> type(a)
<class 'str'>
>>> 
>>> 
>>> a = 3
>>> b = 4
>>> a + b
7
>>> a * b
12
>>> a ** b
81
>>> a/b
0.75
>>> 
>>> 
>>> print "Hello"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello")?
>>> 
