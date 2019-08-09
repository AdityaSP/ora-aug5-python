Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> p='hello'
>>> t = 'hi hello'
>>> re.search(p, t)
<re.Match object; span=(3, 8), match='hello'>
>>> m = re.seach(p,t)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    m = re.seach(p,t)
AttributeError: module 're' has no attribute 'seach'
>>> m = re.search(p,t)
>>> type(m)
<class 're.Match'>
>>> m.start(), m.end()
(3, 8)
>>> t[m.start():m.end()]
'hello'
>>> p='hello'
>>> t = 'hello hi hello'
>>> m = re.search(p,t)
>>> m.start(), m.end()
(0, 5)
>>> re.findall(p,t)
['hello', 'hello']
>>> for m in re.finditer(p,t):
	print("found at: ", m.start(), m.end())

	
found at:  0 5
found at:  9 14
>>> t = 'sasasas'
>>> p = 'sas'
>>> 
>>> re.findall(p,t)
['sas', 'sas']
>>> for m in re.finditer(p,t):
	print("found at: ", m.start(), m.end())

	
found at:  0 3
found at:  4 7
>>> 
>>> 
>>> # char repetition
>>> p = 'xy*'
>>> t = 'xyxyyyxyyyyyyyx'
>>> #* --> 0 or n y
>>> # x followed by 0 or more y
>>> re.findall(p,t)
['xy', 'xyyy', 'xyyyyyyy', 'x']
>>> p = 'xy+'
>>> t = 'xyxyyyxyyyyyyyx'
>>> #+ --> 1 or n y
>>> #x followed by 1 or more y
>>> re.findall(p,t)
['xy', 'xyyy', 'xyyyyyyy']
>>> p = 'xy?'
>>> t = 'xyxyyyxyyyyyyyx'
>>> #? --> 0 or 1 y
>>> #x followed by 0 or 1 y
>>> 
>>> re.findall(p,t)
['xy', 'xy', 'xy', 'x']
>>> p = 'xy{3}'
>>> t = 'xyxyyyxyyyyyyyx'
>>> re.findall(p,t)
['xyyy', 'xyyy']
>>> p = 'xy{1,3}'
>>> t = 'xyxyyyxyyyyyyyx'
>>> re.findall(p,t)
['xy', 'xyyy', 'xyyy']
>>> p = 'x{2}y{3}'
>>> t = 'xyxyyyxyyyyyyyx'
>>> re.findall(p,t)
[]
>>> t = 'xxyyyyyyyyxxyyyyyyy'
>>> re.findall(p,t)
['xxyyy', 'xxyyy']
>>> 
>>> p = 'stabilize'
>>> p1 = 'stabilise'
>>> t = 'stabilize'
>>> t1 = 'stabilise'
>>> p = 'stabili[zs]e'
>>> re.findall(p,t)
['stabilize']
>>> re.findall(p,t1)
['stabilise']
>>> t = 'xyxyyyxyyyyyyyx'
>>> p = '[xy]+'
>>> # one or more occurrances x or y
>>> re.findall(p,t)
['xyxyyyxyyyyyyyx']
>>> t = 'xyxyyyxyayyyyyyx'
>>> re.findall(p,t)
['xyxyyyxy', 'yyyyyyx']
>>> t = 'USD 300'
>>> p = '[0123456789]+'
>>> re.findall(p,t)
['300']
>>> t = 'USD 23984798234'
>>> p = '[0123456789]+'
>>> re.findall(p,t)
['23984798234']
>>> p = '[0-9]+'
>>> re.findall(p,t)
['23984798234']
>>> t = 'Friday friday'
>>> p = '[Ff]{1}riday'
>>> re.findall(p,t)
['Friday', 'friday']
>>> t = 'USD 300'
>>> p = '[A-Z]{3}'
>>> re.findall(p,t)
['USD']
>>> t = 'INR 300'
>>> re.findall(p,t)
['INR']
>>> t = 'inr 300'
>>> re.findall(p,t)
[]
>>> p = '[A-Za-z]{3}'
>>> re.findall(p,t)
['inr']
>>> t = 'INR 300'
>>> re.findall(p,t)
['INR']
>>> 
>>> 
>>> p = '(xy)+'
>>> t = 'xxxxxxyyyyy'
>>> re.findall(p,t)
['xy']
>>> t = 'xyxyxyxyxxx'
>>> re.findall(p,t)
['xy']
>>> for m in re.finditer(p,t):
	print(m.group())

	
xyxyxyxy
>>> d = '10-05-2019'
>>> p = '[0-9]{2}-[0-9]{2}-[0-9]{4}'
>>> re.findall(p,t)
[]
>>> p = r'[0-9]{2}-[0-9]{2}-[0-9]{4}'
>>> re.findall(p,t)
[]
>>> re.findall(p,d)
['10-05-2019']
>>> p = r'([0-9]{2})-([0-9]{2})-([0-9]{4})'
>>> re.findall(p,d)
[('10', '05', '2019')]
>>> t = 'Mfg Date 02-05-2017 Exp Date 03-04-2019'
>>> 
>>> 
>>> p = 'Exp Date [0-9]{2}-[0-9]{2}-[0-9]{4}'
>>> re.findall(p,t)
['Exp Date 03-04-2019']
>>> p = 'Exp Date ([0-9]{2}-[0-9]{2}-[0-9]{4})'
>>> re.findall(p,t)
['03-04-2019']
>>> t = 'Mfg Date 02-05-2017 Ex Date 03-04-2019'
>>> p = 'Exp Date ([0-9]{2}-[0-9]{2}-[0-9]{4})'
>>> re.findall(p,t)
[]
>>> t = 'Mfg Date 02-05-2017 Exp Date 03-04-2019'
>>> re.findall(p,t)
['03-04-2019']
>>> 
>>> 
>>> t = 'http://google.com'
>>> p = 'http|https'
>>> re.findall(p,t)
['http']
>>> t = 'ssh://google.com'
>>> re.findall(p,t)
[]
>>> t = 'https://google.com'
>>> re.findall(p,t)
['http']
>>> 
>>> 
>>> t = 'http://google.com'
>>> p = 'http'
>>> re.findall(p,t)
['http']
>>> t = 'googlehttp://.com'
>>> re.findall(p,t)
['http']
>>> t
'googlehttp://.com'
>>> t = 'http://google.com'
>>> p = '^http'
>>> re.findall(p,t)
['http']
>>> t = 'googlehttp://.com'
>>> re.findall(p,t)
[]
>>> t = 'http://google.com'
>>> p = 'com$'
>>> re.findall(p,t)
['com']
>>> t = 'http://google.us'
>>> re.findall(p,t)
[]
>>> 
>>> 
>>> 
