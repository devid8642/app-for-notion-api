import json
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()
token = getenv('SECRET_API_KEY')

def get_daily_tasks(db, name_db='não informado'):
	url = f'https://api.notion.com/v1/databases/{db}/query'
	headers = {
		"Authorization": f"Bearer {token}",
		"Notion-Version": "2021-08-16",
	}

	r = requests.post(url, headers=headers)

	if r.status_code == 200:
		data = r.json()
		tasks = data['results']
		print(tasks)
	else:
		print(f'A conexão com o banco {name_db} não foi funcionou')

if __name__ == '__main__':
	get_daily_tasks(getenv('DATABASE_FRONT'), 'front')