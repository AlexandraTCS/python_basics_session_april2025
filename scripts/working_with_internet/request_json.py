
import requests
import json
from datetime import datetime

"""
JSON, or JavaScript Object Notation, is a widely-used text-based format for data interchange.
Json basics:
https://www.w3schools.com/whatis/whatis_json.asp
Json with Python documentation:
https://docs.python.org/3/library/json.html
"""


# Data source
#https://earthquake.usgs.gov/earthquakes/feed/

def print_info(data):
    print("Earthquake Information:")
    for feature in data['features'][:3]:  # Display the first 5 earthquakes
        properties = feature['properties']
        print(f"Place: {properties['place']}")
        print(f"Magnitude: {properties['mag']}")
        print(f"Time: {properties['time']}")
        print("-" * 40)    

def get_high_mag(data):
    print("High Magnitude Earthquakes:")
    for feature in data['features']: 
        properties = feature['properties']
        if properties['mag']>5.5:
            print(f"Place: {properties['place']}")
            print(f"Magnitude: {properties['mag']}")            
            print(f"Time: {datetime.fromtimestamp(properties['time']/1000).strftime('%Y-%m-%d %H:%M')}")
            print("-" * 40) 

# Purpose: Fetches JSON data from a URL and saves it to a file
# Specify the URL you want to fetch data from
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

# Make the GET request
response = requests.get(url)

# Check the status code to confirm the request was successful
if response.status_code == 200:
    # Parse the JSON response (if applicable)
    data = response.json()    
#    print_info(data)
    get_high_mag(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

