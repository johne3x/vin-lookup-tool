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
        A string containing all vehicle details formatted, or an error message string.
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

        result_string = ""
        if isinstance(data, list):
            if not data: # Handles empty list
                 return "No data found for this VIN."
            for i, record in enumerate(data):
                if len(data) > 1:
                    result_string += f"--- Record {i+1} ---\n"
                for key, value in record.items():
                    result_string += f"{key.replace('_', ' ').title()}: {value}\n"
        elif isinstance(data, dict):
            if not data: # Handles empty dict
                 return "No data found for this VIN."
            for key, value in data.items():
                result_string += f"{key.replace('_', ' ').title()}: {value}\n"
        else:
            # This case should ideally not be reached if API behaves as expected (list or dict)
            return "Unexpected data format received from API."
        
        return result_string.strip() if result_string else "No data extracted from VIN."

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
            details_string = get_vin_details(vin_input, api_key)
            print(details_string)
        else:
            print("No VIN entered.")
