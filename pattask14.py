# https://restcountries.com/v3.1/all
# Using the class constructer for taking the input of above mentioned url.

class Link:
  def __init__(self, url):
    self.url = url

  def get_url(self):
    return self.url

link = Link(input("https://restcountries.com/v3.1/all"))
print(link.get_url())

# 2. Create a method that willfetch all the JSON data from the URL

import requests

# Send a GET request to the desired API URL
response = requests.get('https://restcountries.com/v3.1/all')

# Parse the response and print it
data = response.json()
print(data)

# 3. Create a method that will display the name of countries, currencies and currency symbol.

import requests

def display_countries_and_currencies():
   
    api_url = 'https://restcountries.com/v3.1/all'

    try:
        # Fetch data from the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            countries_data = response.json()

            # Display country names and currencies
            for country in countries_data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                currency_names = [currency.get('name', 'N/A') for currency in currencies.values()]

                print(f"Country: {name}")
                print(f"Currencies: {', '.join(currency_names)}")
                print('-' * 30)

        else:
            print(f"Error: Unable to fetch data. Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

# Call the method to display countries and currencies
display_countries_and_currencies()

# 4. Create a method that will display the all those countries which currency is dollar 

import requests

def get_countries_using_dollar():
    url = "https://restcountries.com/v2/all"  

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors

        countries_data = response.json()

        # Filter countries where currency is dollar
        dollar_countries = [country['name'] for country in countries_data if 'USD' in [currency['code'] for currency in country.get('currencies', [])]]

        return dollar_countries

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
dollar_countries_list = get_countries_using_dollar()

if dollar_countries_list:
    print("Countries using Dollar as currency:")
    for country in dollar_countries_list:
        print(country)
else:
    print("Failed to retrieve data.")

# 5. Create a method that will display the all those countries which currency is Euro

import requests

def get_countries_with_euro():
    api_url = "https://restcountries.com/v3.1/all"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            countries_data = response.json()

            # Filter countries that use Euro as their currency
            euro_countries = [country['name']['common'] for country in countries_data if 'EUR' in country.get('currencies', {})]

            # Display the list of countries
            if euro_countries:
                print("Countries using Euro as currency:")
                for country in euro_countries:
                    print(country)
            else:
                print("No countries found using Euro as currency.")
        else:
            print(f"Error: Unable to fetch data from the API. Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

# Call the function to get and display countries using Euro
get_countries_with_euro() 

# Visit the url https://www.openbrewerydb.org/
# 1. List the name of all breweries present in the state of Alaska, Maine and NewYork.

import requests

def get_breweries_in_states(states):
    base_url = "https://api.openbrewerydb.org/breweries"
    
    for state in states:
        params = {'by_state': state}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            breweries_data = response.json()
            print(f"\nBreweries in {state}:")
            for brewery in breweries_data:
                print(brewery['name'])
        else:
            print(f"Error: Unable to fetch data for {state}. Status Code: {response.status_code}")

if __name__ == "__main__":
    # List of states: Alaska, Maine, New York
    states_to_query = ['Alaska', 'Maine', 'New York']
    get_breweries_in_states(states_to_query)
