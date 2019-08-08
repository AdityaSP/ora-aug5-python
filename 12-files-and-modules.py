Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> fp = 'D:\\training\\python\\trial.txt'
>>> fp = 'D:/training/python/trial.txt'
>>> fp = r'D:\training\python\trial.txt'
>>> fh = open(fp, 'wt')
>>> fh.write("Line 1")
6
>>> fh.close()
>>> fh.write("Line 2")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fh.write("Line 2")
ValueError: I/O operation on closed file.
>>> fh = open(fp, 'wt')
>>> fh.write("Line 1")
6
>>> fh.write("Line 2")
6
>>> fh.close()
>>> fh = open(fp, 'wt')
>>> fh.write("Line 1\n")
7
>>> fh.write("Line 2\n")
7
>>> fh.close()
>>> fh = open(fp, 'at')
>>> fh.write("Line 3\n")
7
>>> fh.close()
>>> fh = open(fp, 'rt')
>>> fh.write("Line 3\n")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fh.write("Line 3\n")
io.UnsupportedOperation: not writable
>>> s = fh.read()
>>> s
'Line 1\nLine 2\nLine 3\n'
>>> s = fh.read()
>>> s
''
>>> fh.tell()
24
>>> fh.seek(0)
0
>>> fh.tell()
0
>>> s = fh.read()
>>> s
'Line 1\nLine 2\nLine 3\n'
>>> fh.tell()
24
>>> fh.seek(0)
0
>>> s = fh.read(10)
>>> s
'Line 1\nLin'
>>> fh.tell()
11
>>> fh.read()
'e 2\nLine 3\n'
>>> fh.tell()
24
>>> fh.seek(0)
0
>>> lines = fh.readlines()
>>> lines
['Line 1\n', 'Line 2\n', 'Line 3\n']
>>> fh.seek(0)
0
>>> for line in fh:
	print(line)

	
Line 1

Line 2

Line 3

>>> fh.close()
>>> 
