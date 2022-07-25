import requests
import pandas as pd
from pandas import DataFrame

page = 1
API_KEY = '87f9089b3a11b7d2892ac223fe6da184'
API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page={page}'

request_data = requests.get(API_URL).json()
# print(request_data)
print(request_data['results'])

table_data = pd.DataFrame(request_data)
table_data