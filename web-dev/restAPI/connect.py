import requests
import pprint
import  pandas as pd
api_key = '8c0416981bd8a26233be9dffef406fd8'
api_key_v4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YzA0MTY5ODFiZDhhMjYyMzNiZTlkZmZlZjQwNmZkOCIsInN1YiI6IjVlYWU3NGFmMjdkOWNjMDAxYmQwZDJkOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3nZSSkndaEE5N89URYT3AG9YQHsBdztICeMj2I24l_Y'

# Using version 3
api_version = 3
movie_id = 501
# api_base_url = f'https://api.themoviedb.org/{api_version}'
# endpoint_path = f'/movie/{movie_id}'
# endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
# headers = {
#            'Authorization': f'Bearer {api_key_v4}',
#            'Content-Type': 'application/json;charset=utf-8'}

# r  = requests.get(endpoint, headers=headers)
# print(r.status_code)
# print(r.text)


api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query=Matrix'
print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())

if r.status_code in range (200,999):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))

output = 'restAPI/movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f'/movie/{movie_id}'
    endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
    r = requests.get(endpoint)
    if r.status_code in range(200,999):
        data= r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index = False)