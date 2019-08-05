Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [34,56,12]
>>> len(li)
3
>>> li[0]
34
>>> li[2]
12
>>> li[5]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    li[5]
IndexError: list index out of range
>>> li[0:]
[34, 56, 12]
>>> a = "Hope lives on to let you hope"
>>> li = a.split()
>>> li
['Hope', 'lives', 'on', 'to', 'let', 'you', 'hope']
>>> li[5:]
['you', 'hope']
>>> li[::-1]
['hope', 'you', 'let', 'to', 'on', 'lives', 'Hope']
>>> 
>>> s = "hello"
>>> s[0]='D'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s[0]='D'
TypeError: 'str' object does not support item assignment
>>> s = "Hi"
>>> id(s)
2292497757104
>>> s = "hello"
>>> id(s)
2292497758000
>>> l
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> li
['Hope', 'lives', 'on', 'to', 'let', 'you', 'hope']
>>> id(li)
2292497821064
>>> li[2]='ON'
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope']
>>> id(li)
2292497821064
>>> 
>>> 
>>> li.append('Smile')
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope', 'Smile']
>>> b = ['Hello','Hi','How']
>>> len(li)
8
>>> len(b)
3
>>> li.extend(b)
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope', 'Smile', 'Hello', 'Hi', 'How']
>>> li = ['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope']
>>> len(li)
7
>>> li.append(b)
>>> len(li)
8
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope', ['Hello', 'Hi', 'How']]
>>> li[7]
['Hello', 'Hi', 'How']
>>> li[7][2]
'How'
>>> li[-1][-1]
'How'
>>> li[-1][-1][-1][-1][-1]
'w'
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope', ['Hello', 'Hi', 'How']]
>>> li.extend('Smile')
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope', ['Hello', 'Hi', 'How'], 'S', 'm', 'i', 'l', 'e']
>>> li = ['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope']
>>> li.insert(3,'Smile')
>>> li
['Hope', 'lives', 'ON', 'Smile', 'to', 'let', 'you', 'hope']
>>> # item based li[0]="Hello"
>>> # append to a list li.append("Smile")
>>> # extend to a list li.extend([1,2,3])
>>> # insert at any location li.insert(3,"Smile")
>>> li.insert(-1, "Smile")
>>> li
['Hope', 'lives', 'ON', 'Smile', 'to', 'let', 'you', 'Smile', 'hope']
>>> 
>>> 
>>> li.remove('Smile')
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'Smile', 'hope']
>>> a
'Hope lives on to let you hope'
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> del li[-2]
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope']
>>> li.pop()
'hope'
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you']
>>> li.pop(1)
'lives'
>>> li
['Hope', 'ON', 'to', 'let', 'you']
>>> li = ['Hope', 'lives', 'ON', 'Smile', 'to', 'let', 'you', 'Smile', 'hope']
>>> li.count('Smile')
2
>>> for i in range(li.count('Smile')):
	li.remove('Smile')

	
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'hope']
>>> li.insert(-1, "Smile")
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'Smile', 'hope']
>>> li.append('Smile')
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'Smile', 'hope', 'Smile']
>>> li.insert(1000, 'Smile')
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'Smile', 'hope', 'Smile', 'Smile']
>>> li.insert(len(li), 'x')
>>> li
['Hope', 'lives', 'ON', 'to', 'let', 'you', 'Smile', 'hope', 'Smile', 'Smile', 'x']
>>> 
