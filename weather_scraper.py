import requests
import argparse
import sys
from bs4 import BeautifulSoup

# usage:    python basic_weather_scraper.py 32603 --unit C

# output formatting to look nice
line = "*" + " " * 58 + "*"

print("*" * 60)
print(line)
print("*{:^58}*".format('CLI Client for Weather Scraper'))  # centered title
print(line)
print("*" * 60)

# parser to handle cl arguments
parser = argparse.ArgumentParser(description='A weather scraper CLI tool.')

# location argument
parser.add_argument('location', help='The city/zipcode to scrape a weather forecast for.')

# argument flags for temperature units
parser.add_argument(
    '--unit',
    choices=['C','F'],
    default='F',
    help="Temperature units: F for Farenheit, C for Celsius (Default is set to: F)."
)

args = parser.parse_args()

location = args.location
unit = args.unit

print(line)
print("*{:^58}*".format("Fetching weather for: " + str(location)))  # centered title
print("*{:^58}*".format("Temperature unit: " + str(unit)))
print(line)


# TODO: checks for valid input needs adjustments


url = "https://forecast.weather.gov/zipcity.php"

params = {

    "inputstring": location
}

# send request to download html content into a request obj
response = requests.get(url, params=params)

# if the the request response is successful
if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # choose class based off user input
    temp_class_name = "myforecast-current-lrg" if unit == 'F' else "myforecast-current-sm"
    temp_element = soup.find('p', class_=temp_class_name)
    temperature = temp_element.get_text(strip=True)

    print("*" * 60)
    print(line)
    print("*{:^58}*".format("Temperature: " + str(temperature)))  # centered title
    # condtions stored in a table within this parent div

    conditions_div = soup.find('div', id='current_conditions_detail')
    rows = conditions_div.find_all('tr')

    for row in rows:
        # gets the label from the first <td>
        label = row.find('td', class_='text-right').get_text(strip=True)
        # gets data from the second <td>
        value = row.find_all('td')[1].get_text(strip=True)

        print("*{:^58}*".format(label + ": " + str(value)))  # centered title

    print(line)
    print("*" * 60)


else:
    print(f"Failed to collect weather data. Status code: {response.status_code}")
    sys.exit()




