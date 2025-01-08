import requests
import argparse
import sys
from bs4 import BeautifulSoup

#   Weather Scraper for Weather.gov
#                V 1.0
#           by Ethan Wilson

# usage:    python weather_scraper.py 32603 --unit C

# output formatting to look nice

def get_weather_data(location, unit):
    url = "https://forecast.weather.gov/zipcity.php"
    params = {"inputstring": location}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather data. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup



line = "*" + " " * 58 + "*"

print("*" * 60)
print(line)
print("*{:^58}*".format('CLI Client for Weather Scraper'))  # centered title
print(line)
print("*" * 60)

# parser to handle cl arguments
parser = argparse.ArgumentParser(description='A weather scraper CLI tool.')

# location argument
parser.add_argument(
    'location',
    nargs='?',
    default='32603', # default zip code          
    help='The city/zipcode to scrape a weather forecast for. Default is 32603')

# argument flags for temperature units
parser.add_argument(
    '--unit',
    choices=['C','F'],
    default='F',
    help="Temperature units: F for Fahrenheit, C for Celsius (Default is set to: F)."
)

args = parser.parse_args()

location = args.location
unit = args.unit

# check for valid zip code or city input
if not location.isdigit() and len(location) != 5 and not location.isalpha():
    print("Invalid location. Please provide a valid ZIP code or city.")
    sys.exit()


print(line)
print("*{:^58}*".format("Fetching weather for: " + str(location)))  # centered title
print("*{:^58}*".format("Temperature unit: " + str(unit)))
print(line)
print("*" * 60)




try:
    soup = get_weather_data(location, unit)

except Exception as e:
    print(e)
    sys.exit()


# choose class based off user input
temp_class_name = "myforecast-current-lrg" if unit == 'F' else "myforecast-current-sm"
temp_element = soup.find('p', class_=temp_class_name)

#check for website change
if not temp_element:
    print("Temperature data not found. Please check the location & try again.")
    sys.exit()

temperature = temp_element.get_text(strip=True)


print(line)
print("*{:^58}*".format("Temperature: " + str(temperature)))
# condtions stored in a table within this parent div

conditions_div = soup.find('div', id='current_conditions_detail')

if not conditions_div:
    print("Weather conditions data not found.")
    sys.exit()


rows = conditions_div.find_all('tr')

for row in rows:
    # gets the label from the first <td>
    label = row.find('td', class_='text-right').get_text(strip=True)
    # gets data from the second <td>
    value = row.find_all('td')[1].get_text(strip=True)

    # center additional weather data
    print("*{:^58}*".format(label + ": " + str(value)))  # center additional weather data

print(line)
print("*" * 60)






