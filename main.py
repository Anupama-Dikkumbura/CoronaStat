import requests
import json
from datetime import datetime

input_country = input("Enter Country: ")
url = f"https://disease.sh/v3/covid-19/countries/{input_country}"

try:
    response = requests.get(url).text
    country = json.loads(response)
    if response:
        print(f"Country: {country['country']} Updated at: {datetime.fromtimestamp(country['updated']/1000).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Cases: {country['cases']}")
        print(f"Total Deaths: {country['deaths']}")
        print(f"Total Recovered: {country['recovered']}")
except:
    print("COUNTRY NOT FOUND")
