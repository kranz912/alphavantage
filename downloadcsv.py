import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = """https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=^DJI&outputsize=full&apikey=38JSBGW4H2GJ8S6A"""

file = requests.get(url=url,headers=headers)


open('^DJI.json','wb').write(file.content)
