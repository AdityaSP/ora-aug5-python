Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Strings
>>> s = "Hello World"
>>> type(s)
<class 'str'>
>>> s + " Again"
'Hello World Again'
>>> s1 = s + " Again"
>>> s1
'Hello World Again'
>>> s
'Hello World'
>>> #s = s + " Again"
>>> s += " Again"
>>> s
'Hello World Again'
>>> s
'Hello World Again'
>>> s + 3
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s + 3
TypeError: can only concatenate str (not "int") to str
>>> a = "5"
>>> b = 3
>>> a + b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a + b
TypeError: can only concatenate str (not "int") to str
>>> int(a) + b
8
>>> a + str(b)
'53'
>>> s = "Hello"
>>> s * 3
'HelloHelloHello'
>>> print("-" * 50)
--------------------------------------------------
>>> ############## String as sequence #############
>>> 
>>> 
>>> s = "Hello World"
>>> len(s)
11
>>> s[0]
'H'
>>> s[10]
'd'
>>> s[11]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s[11]
IndexError: string index out of range
>>> s[-1]
'd'
>>> s[-11]
'H'
>>> s[-12]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[-12]
IndexError: string index out of range
>>> 
>>> ### Slicing ###
>>> s
'Hello World'
>>> len(s)
11
>>> s[0:5]
'Hello'
>>> s[6:10]
'Worl'
>>> s[6:11]
'World'
>>> s[6:100]
'World'
>>> s[-1:-5]
''
>>> s[-5:-1]
'Worl'
>>> s[0:100:1]
'Hello World'
>>> s[0:100:2]
'HloWrd'
>>> s[-5:-1:1]
'Worl'
>>> s[-1:-5:1]
''
>>> s[-1:-5:-1]
'dlro'
>>> s
'Hello World'
>>> s[1:-1]
'ello Worl'
>>> s[6:-9]
''
>>> s[-1:0]
''
>>> s[0:-1]
'Hello Worl'
>>> s[-1:0:-1]
'dlroW olle'
>>> a = '0123456789'
>>> a[-1:0:-1]
'987654321'
>>> a[0:10:-1]
''
>>> a[-1:-10:-1]
'987654321'
>>> a[-1:-11:-1]
'9876543210'
>>> a[-1:-len(a)-1:-1]
'9876543210'
>>> a = "Hope lives on to let you hope"
>>> a[-1:-len(a)-1:-1]
'epoh uoy tel ot no sevil epoH'
>>> s
'Hello World'
>>> s[6:100]
'World'
>>> s[6:]
'World'
>>> s[6::2]
'Wrd'
>>> s[0:5]]
SyntaxError: invalid syntax
>>> s[0:5]
'Hello'
>>> s[:5]
'Hello'
>>> s[:]
'Hello World'
>>> s[::]
'Hello World'
>>> s[::-1]
'dlroW olleH'
>>> a = "Hope lives on to let you hope"
>>> a[-1:-len(a)-1:-1]
'epoh uoy tel ot no sevil epoH'
>>> a[::-1]
'epoh uoy tel ot no sevil epoH'
>>> # syntactic shorthand is also called as syntactic sugars
>>> 

>>> ############## Strings as objects ##############
>>> s
'Hello World'
>>> s.upper()
'HELLO WORLD'
>>> a = 10
>>> s.lower()
'hello world'
>>> s.count('o')
2
>>> s.isalpha()
False
>>> "hello".isalpha()
True
>>> a = "Hope lives on to let you hope"
>>> a.split()
['Hope', 'lives', 'on', 'to', 'let', 'you', 'hope']
>>> s = "192.168.99.100"
>>> s.split('.')
['192', '168', '99', '100']
>>> s ="hello::what::where"
>>> s.split("::")
['hello', 'what', 'where']
>>> a = "Hope lives on to let you hope"
>>> a.split()
['Hope', 'lives', 'on', 'to', 'let', 'you', 'hope']
>>> a.split(" ")
['Hope', 'lives', 'on', 'to', 'let', 'you', 'hope']
>>> a = "Hello  How"
>>> a.split()
['Hello', 'How']
>>> a.split(' ')
['Hello', '', 'How']
>>> s = "conhost.exe                  23756 Console                    2     18,648 K"
>>> s.split(" ")
['conhost.exe', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '23756', 'Console', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2', '', '', '', '', '18,648', 'K']
>>> s.split()
['conhost.exe', '23756', 'Console', '2', '18,648', 'K']
>>> a = "Hope lives on to let you hope"
>>> a.split()
['Hope', 'lives', 'on', 'to', 'let', 'you', 'hope']
>>> ans = a.split()
>>> type(ans)
<class 'list'>
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> help(s.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.

>>> len.__doc__
'Return the number of items in a container.'
>>> s.split.__doc__
'Return a list of the words in the string, using sep as the delimiter string.\n\n  sep\n    The delimiter according which to split the string.\n    None (the default value) means split according to any whitespace,\n    and discard empty strings from the result.\n  maxsplit\n    Maximum number of splits to do.\n    -1 (the default value) means no limit.'
>>> # __ = double underscore = dunder
>>> s.zfill.__doc__
'Pad a numeric string with zeros on the left, to fill a field of the given width.\n\nThe string is never truncated.'
>>> s = 10
>>> s = "10"
>>> s.zfill(5)
'00010'
>>> s = "hello"
>>> s.zfill(10)
'00000hello'
>>> 
