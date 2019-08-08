import json
fp = r'D:\training\python\ora-aug5-python\prog\json.data'
fh = open(fp, 'rt')
jsonstr = fh.read()
movie_data = json.loads(jsonstr)
print(type(movie_data))
print(movie_data.keys())

for movie in movie_data['Search']:
    print(movie['Poster'])