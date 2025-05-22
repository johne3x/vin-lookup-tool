import requests
import os
import sys # Added for sys.exit()
from dotenv import load_dotenv

def get_vin_details(vin, api_key):
    """
    Retrieves vehicle details for a given VIN using the API Ninjas VIN Lookup API.

    Args:
        vin: The Vehicle Identification Number (string).
        api_key: The API key for API Ninjas (string).

    Returns:
        A dictionary with make, model, and year, or an error message string.
    """
    api_url = f"https://api.api-ninjas.com/v1/vinlookup?vin={vin}"
    headers = {'X-Api-Key': api_key}

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code != 200:
            return f"Error: API returned status code {response.status_code} - {response.text}"

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            return "Error: Could not decode JSON response from API."

        if not data: # Handles empty list or empty dict
            return "No data found for this VIN."

        # API returns a list of matching VINs, even if it's just one.
        # If it's a dictionary for some reason, or an empty list, handle that.
        if isinstance(data, list) and data:
            vehicle_info = data[0] # Assuming the first result is the most relevant
        elif isinstance(data, dict) and data: # Fallback if API returns a single dict directly
            vehicle_info = data
        else: # Handles empty list or other unexpected non-empty but unusable data types
            return "No data found for this VIN."

        return {
            'make': vehicle_info.get('make'),
            'model': vehicle_info.get('model'),
            'year': vehicle_info.get('year')
        }

    except requests.exceptions.RequestException as e:
        return f"Error: API request failed: {e}"


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_NINJAS_KEY")

    if not api_key: # Check if api_key is None or empty
        print("Error: API_NINJAS_KEY not found in .env file. Please make sure it is set.")
        sys.exit(1) # Exit the script
    else:
        vin_input = input("Enter VIN: ")
        if vin_input:
            details = get_vin_details(vin_input, api_key)
            if isinstance(details, dict):
                print(f"Make: {details.get('make', 'N/A')}, Model: {details.get('model', 'N/A')}, Year: {details.get('year', 'N/A')}")
            else:
                print(details)
        else:
            print("No VIN entered.")
