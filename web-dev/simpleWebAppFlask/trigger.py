import requests

ngrok_url = 'http://3f9f7997.ngrok.io'
endpoint = f'{ngrok_url}/box-office-scraper'


r = requests.post(endpoint, json ={})
print(r.json()['data'])