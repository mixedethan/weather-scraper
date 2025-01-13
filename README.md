# CLI Weather Scraper

# Brought into Existence by Ethan Wilson

**Version 1.0**

A Python CLI tool to pull current weather data from [Weather.gov](https://www.weather.gov) based on a inputted city or ZIP code. This tool provides temperature, humidity, wind speed, and other weather conditions in a  formatted way.

---

## Features
- Pulls temperature (Celsius or Fahrenheit) and additional weather data like humidity and wind speed.
- Command-line interface (CLI) with user-friendly arguments.
- Compatible with any operating system running Python 3.7+.

---

## Requirements
To use this project, ensure you have:
- Python 3.7 or later installed
- Internet connection (for fetching data from Weather.gov)

---

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/mixedethan/weather_scraper.git
   cd weather_scraper
   

2. Install dependencies:
   bash
   pip install -r requirements.txt
   

3. Run the script:
   bash
   python weather_scraper.py <location> [--unit C|F]
   

---

## Usage
```bash
python weather_scraper.py <location>
```
- Replace `<location>` with a ZIP code (e.g., `32603`) or a city name (e.g., `Gainesville`).

### Temperature Unit (Optional)
- Use the `--unit` flag to specify Celsius or Fahrenheit (default: Fahrenheit):
  ```bash
  python weather_scraper.py <location> --unit C
  ```

### Example Commands
```bash
python weather_scraper.py 32603
python weather_scraper.py "Gainesville" --unit C
```

---

## Output
Example output for `python weather_scraper.py 32603 --unit F`:
```
************************************************************
*                                                          *
*              CLI Client for Weather Scraper              *
*                                                          *
************************************************************
*             Fetching weather for: 32603                 *
*             Temperature unit: F                         *
************************************************************
************************************************************
*              Temperature: 68°F                          *
*              Humidity: 50%                               *
*              Wind Speed: N 10 mph                       *
************************************************************
```

---

## Limitations
- This tool relies on the current structure (as of 1/2025) of [Weather.gov](https://www.weather.gov). Changes to their HTML may break the scraper.
- Requires an internet connection to pull weather data.

---

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

---

## Thank you for reading
