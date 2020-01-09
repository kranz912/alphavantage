import requests
import sys


print(sys.argv)

symbol =  sys.argv[1]

if symbol != None:

    apikey = '38JSBGW4H2GJ8S6A'


    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = """https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}""".format(symbol,apikey)

    file = requests.get(url=url,headers=headers)


    open('{}.json'.format(symbol),'wb').write(file.content)

else:
    print('missing parameters')
