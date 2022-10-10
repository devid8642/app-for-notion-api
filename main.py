import json
import requests
from datetime import date as dt
from dotenv import load_dotenv
from os import getenv

def list_daily_tasks(list_tasks):
	for task in list_tasks:
		print(f'-> {task}')

def get_daily_tasks(list_db, token):
	today = str(dt.today())
	headers = {
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json',
		'Notion-Version': '2022-06-28',
	}
	list_tasks = []

	for db in list_db:
		url = f'https://api.notion.com/v1/databases/{db}/query'

		r = requests.post(url, headers=headers)

		if r.status_code == 200:
			dataset = r.json()
			tasks = dataset['results']

			for task in tasks:
				name = task['properties']['Nome']['title'][0]['plain_text']
				date = task['properties']['Data']['date']['start']

				if date == today:
					list_tasks.append(name)
		else:
			print('conexão com um banco falhou')

	return list_tasks

if __name__ == '__main__':
	load_dotenv()
	token = getenv('SECRET_API_KEY')
	dbs = [getenv('DATABASE_FRONT'), getenv('DATABASE_BACK'), getenv('DATABASE_SCHOOL')]
	tasks = get_daily_tasks(dbs, token)
	list_daily_tasks(tasks)