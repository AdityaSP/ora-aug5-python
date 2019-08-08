import json
#fp = r'D:\training\python\ora-aug5-python\prog\json.data'
#fh = open(fp, 'rt')
#jsonstr = fh.read()
#movie_data = json.loads(jsonstr)
import requests
r = requests.get('http://www.omdbapi.com/?s=spiderman&apikey=b4e17ea0')

if r.ok:
    movie_data=r.json()

    for movie in movie_data['Search']:
        if movie['Poster'] != 'N/A':
            print ("Downloading", movie['Poster'])
            poster = requests.get(movie['Poster'])
            if poster.ok:
                fh = open(movie['imdbID'] +'.jpg' ,'wb') 
                fh.write(poster.content)
                fh.close()
                