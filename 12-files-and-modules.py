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
>>> 
>>> 
>>> 
>>> import requests
>>> r = requests.get('http://www.omdbapi.com/?s=batman&apikey=b4e17ea0')
>>> r.status_code
200
>>> r.ok
True
>>> r = requests.get('http://www.omdbapi.com/?s=batman&apikey=b4')
>>> r.status_code
401
>>> r.ok
False
>>> r = requests.get('http://www.omdbapi.com/?s=batman&apikey=b4e17ea0')
>>> r.status_code
200
>>> r.ok
True
>>> r.json
<bound method Response.json of <Response [200]>>
>>> r.json()
{'Search': [{'Title': 'Batman Begins', 'Year': '2005', 'imdbID': 'tt0372784', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BZmUwNGU2ZmItMmRiNC00MjhlLTg5YWUtODMyNzkxODYzMmZlXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SX300.jpg'}, {'Title': 'Batman v Superman: Dawn of Justice', 'Year': '2016', 'imdbID': 'tt2975590', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'}, {'Title': 'Batman', 'Year': '1989', 'imdbID': 'tt0096895', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_SX300.jpg'}, {'Title': 'Batman Returns', 'Year': '1992', 'imdbID': 'tt0103776', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BOGZmYzVkMmItM2NiOS00MDI3LWI4ZWQtMTg0YWZkODRkMmViXkEyXkFqcGdeQXVyODY0NzcxNw@@._V1_SX300.jpg'}, {'Title': 'Batman Forever', 'Year': '1995', 'imdbID': 'tt0112462', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNDdjYmFiYWEtYzBhZS00YTZkLWFlODgtY2I5MDE0NzZmMDljXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg'}, {'Title': 'Batman & Robin', 'Year': '1997', 'imdbID': 'tt0118688', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMGQ5YTM1NmMtYmIxYy00N2VmLWJhZTYtN2EwYTY3MWFhOTczXkEyXkFqcGdeQXVyNTA2NTI0MTY@._V1_SX300.jpg'}, {'Title': 'The Lego Batman Movie', 'Year': '2017', 'imdbID': 'tt4116284', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTcyNTEyOTY0M15BMl5BanBnXkFtZTgwOTAyNzU3MDI@._V1_SX300.jpg'}, {'Title': 'Batman: The Animated Series', 'Year': '1992–1995', 'imdbID': 'tt0103359', 'Type': 'series', 'Poster': 'https://m.media-amazon.com/images/M/MV5BOTM3MTRkZjQtYjBkMy00YWE1LTkxOTQtNDQyNGY0YjYzNzAzXkEyXkFqcGdeQXVyOTgwMzk1MTA@._V1_SX300.jpg'}, {'Title': 'Batman: Under the Red Hood', 'Year': '2010', 'imdbID': 'tt1569923', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BYTdlODI0YTYtNjk5ZS00YzZjLTllZjktYmYzNWM4NmI5MmMxXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg'}, {'Title': 'Batman: The Dark Knight Returns, Part 1', 'Year': '2012', 'imdbID': 'tt2313197', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMzIxMDkxNDM2M15BMl5BanBnXkFtZTcwMDA5ODY1OQ@@._V1_SX300.jpg'}], 'totalResults': '366', 'Response': 'True'}
>>> 
