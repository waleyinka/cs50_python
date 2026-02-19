# Task: https://cs50.harvard.edu/python/psets/4/bitcoin/

import sys
import requests

def main():
    # Ensure exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Convert the argument to a float
        number_of_bitcoins = float(sys.argv[1])
    
    except ValueError:
        # Exit early if conversion fails (non-numeric input)
        sys.exit("Invalid number of Bitcoins")

    # CoinCap API endpoint for fetching the current Bitcoin price in USD
    api_url = (
        "https://rest.coincap.io/v3/assets/bitcoin"
        "?apiKey=YourApiKey"
    )

    try:
        # Make a GET request to the CoinCap API with a timeout for safety
        response = requests.get(api_url, timeout=30)

        # Raise an exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()

        # Parse the JSON payload returned by the API
        payload = response.json()

        # Extract and convert the Bitcoin price from string to float
        price_usd = float(payload["data"]["priceUsd"])

    except requests.RequestException:
        # Handles network issues, timeouts, and HTTP errors
        sys.exit("Error fetching Bitcoin price")

    except (KeyError, TypeError, ValueError):
        # Handles unexpected API structure or invalid data formats
        sys.exit("Unexpected API response")

    # Calculate the total cost based on current Bitcoin price
    total_cost = number_of_bitcoins * price_usd

    # Output the cost formatted as USD with commas and four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()