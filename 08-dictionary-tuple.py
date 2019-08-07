Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [1,2,3]
>>> li[0]
1
>>> #username=scott, password=tiger
>>> d = {'username': 'scott', 'password': 'tiger'}
>>> len(d)
2
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['username']
'scott'
>>> d['password']
'tiger'
>>> d ={0:1, 1:2, 2:3}
>>> li[0]
1
>>> d[0]
1
>>> d = {'name':'Aditya', 'city':'Bengaluru'}
>>> d.keys()
dict_keys(['name', 'city'])
>>> d.values()
dict_values(['Aditya', 'Bengaluru'])
>>> d['phone']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d['phone']
KeyError: 'phone'
>>> d['phone']='9018230983'
>>> d
{'name': 'Aditya', 'city': 'Bengaluru', 'phone': '9018230983'}
>>> d['city']='Mysore'
>>> d
{'name': 'Aditya', 'city': 'Mysore', 'phone': '9018230983'}
>>> del d['phone']
>>> d
{'name': 'Aditya', 'city': 'Mysore'}
>>> d['phone']=['9230984234234','342342234']
>>> d
{'name': 'Aditya', 'city': 'Mysore', 'phone': ['9230984234234', '342342234']}
>>> d['phone']
['9230984234234', '342342234']
>>> d['phone'][-1]
'342342234'
>>> d['address']={'home': 'asdfasd sdfasdf', 'work': 'asdklfj weruoidf'}
>>> d
{'name': 'Aditya', 'city': 'Mysore', 'phone': ['9230984234234', '342342234'], 'address': {'home': 'asdfasd sdfasdf', 'work': 'asdklfj weruoidf'}}
>>> d['address']['work']
'asdklfj weruoidf'
>>> 
>>> 
>>> 
>>> 
>>> data = '{
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "MSFT",
        "3. Last Refreshed": "2019-08-07 11:50:20",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2019-08-07": {
            "1. open": "133.7900",
            "2. high": "135.1900",
            "3. low": "131.8284",
            "4. close": "133.7700",
            "5. volume": "13415403"
        },
        "2019-08-06": {
            "1. open": "133.8000",
            "2. high": "135.6800",
            "3. low": "133.2100",
            "4. close": "134.6900",
            "5. volume": "32511217"
        }
    }
}'
SyntaxError: EOL while scanning string literal
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> data = '{     "Meta Data": {         "1. Information": "Daily Prices (open, high, low, close) and Volumes",         "2. Symbol": "MSFT",         "3. Last Refreshed": "2019-08-07 11:50:20",         "4. Output Size": "Compact",         "5. Time Zone": "US/Eastern"     },     "Time Series (Daily)": {         "2019-08-07": {             "1. open": "133.7900",             "2. high": "135.1900",             "3. low": "131.8284",             "4. close": "133.7700",             "5. volume": "13415403"         },         "2019-08-06": {             "1. open": "133.8000",             "2. high": "135.6800",             "3. low": "133.2100",             "4. close": "134.6900",             "5. volume": "32511217"         }     } }'
>>> type(data)
<class 'str'>
>>> import json
>>> d = json.loads(data)
>>> type(d)
<class 'dict'>
>>> d.keys()
dict_keys(['Meta Data', 'Time Series (Daily)'])
>>> type(d['Meta Data'])
<class 'dict'>
>>> d['Meta Data'].keys()
dict_keys(['1. Information', '2. Symbol', '3. Last Refreshed', '4. Output Size', '5. Time Zone'])
>>> d['Meta Data']['1. Information']
'Daily Prices (open, high, low, close) and Volumes'
>>> d['Time Series (Daily)']
{'2019-08-07': {'1. open': '133.7900', '2. high': '135.1900', '3. low': '131.8284', '4. close': '133.7700', '5. volume': '13415403'}, '2019-08-06': {'1. open': '133.8000', '2. high': '135.6800', '3. low': '133.2100', '4. close': '134.6900', '5. volume': '32511217'}}
>>> d['Time Series (Daily)']['2019-08-07']['1. open']
'133.7900'
>>> 
