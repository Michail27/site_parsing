import requests
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
country = "Belarus"
endpoint = f"https://api.covid19api.com/country/{country}/status/confirmed"
params = {"from": str(yesterday), "to": str(today)}

response = requests.get(endpoint, params=params).json()
total_confirmed = 0
for day in response:
    cases = day.get("Cases", 0)
    total_confirmed += cases

print(f"Total Confirmed Covid-19 cases in {country}: {total_confirmed}")