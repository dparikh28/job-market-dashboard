import requests

APP_ID = "e62c10fb"
APP_KEY = "91c08cad9f5862ad3b190f29fdd3b9cb"

url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

params = {
	"app_id": APP_ID,
	"app_key": APP_KEY,
	"what": "data analyst",
	"where": "new york"
}

response = requests.get(url, params=params)
#print(response.status_code)
#print(response.json())

data = response.json()
jobs = data["results"]

for job in jobs:
	title = job["title"]
	company = job["company"]["display_name"]
	location = job["location"]["display_name"]
	salary_min = job.get("salary_min")
	salary_max = job.get("salary_max")
	
	#print(title, " | ", company, " | ", location, " | ", salary_min, "-", salary_max)

import pandas as pd

row = []

for job in jobs:
	row.append({
		"Title": job["title"],
		"Company": job["company"]["display_name"],
		"Location": job["location"]["display_name"],
		"Min Salary": job.get("salary_min"),
		"Max Salary": job.get("salary_max")
	})

df = pd.DataFrame(row)
print(df)
