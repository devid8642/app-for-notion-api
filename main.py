import json
import requests
from datetime import date as dt
from dotenv import load_dotenv
from os import getenv

load_dotenv()
token = getenv('SECRET_API_KEY')

def get_daily_tasks(db, name_db='não informado'):
	today = str(dt.today())
	url = f'https://api.notion.com/v1/databases/{db}/query'
	headers = {
		"Authorization": f"Bearer {token}",
		"Notion-Version": "2021-08-16",
	}

	r = requests.post(url, headers=headers)

	if r.status_code == 200:
		dataset = r.json()
		tasks = dataset['results']

		for task in tasks:
			name = task['properties']['Nome']['title'][0]['plain_text']
			date = task['properties']['Data']['date']['start']

			if date == today:
				print(name)
	else:
		print(f'A conexão com o banco {name_db} não funcionou')

if __name__ == '__main__':
	get_daily_tasks(getenv('DATABASE_FRONT'), 'front')
	get_daily_tasks(getenv('DATABASE_BACK'), 'back')