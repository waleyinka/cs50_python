# Bitcoin Price Index

# Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank,
# Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

# Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

# In a file called bitcoin.py, implement a program that:

 # - Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy.
 #   If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

 # - Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with
 #   the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price
 #   of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
    #   import requests
    #       try:
    #           ...
    #       except requests.RequestException:
    #           sys.exit("Network error")

# Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.


# ===============================================================================


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


# Entry point guard to allow safe imports without execution
if __name__ == "__main__":
    main()