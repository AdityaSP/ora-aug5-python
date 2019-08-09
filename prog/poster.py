import json
import time
import threading
#fp = r'D:\training\python\ora-aug5-python\prog\json.data'
#fh = open(fp, 'rt')
#jsonstr = fh.read()
#movie_data = json.loads(jsonstr)
import requests
r = requests.get('http://www.omdbapi.com/?s=batman&apikey=b4e17ea0')


def download(url, imdbid):
    #print ("Downloading", url)
    poster = requests.get(url)
    if poster.ok:
        with open(imdbid +'.jpg' ,'wb') as fh:
            fh.write(poster.content)


if r.ok:
    movie_data=r.json()
    lot = []
    st = time.time()
    for movie in movie_data['Search']:
        if movie['Poster'] != 'N/A':
            t = threading.Thread(target=download, args=(movie['Poster'], movie['imdbID']))
            lot.append(t)
            t.start()
    
    for t in lot:
        t.join()
        
    et = time.time()
    print("TOOK", et -st)

if r.ok:
    movie_data=r.json()

    st = time.time()
    for movie in movie_data['Search']:
        if movie['Poster'] != 'N/A':
            download(movie['Poster'], movie['imdbID'])
    
    et = time.time()
    print("TOOK", et -st)