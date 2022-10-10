import requests
from datetime import datetime
response = requests.get(url='https://worldtimeapi.org/api/timezone/Europe/Moscow')
data_time = response.json()
unix_time = data_time.get('unixtime')
time = datetime.utcfromtimestamp(int(unix_time)).strftime('%A, %d.%m.%y %H:%M')