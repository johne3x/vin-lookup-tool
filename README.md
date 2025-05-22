# VIN Lookup Application

## Description
This application allows you to fetch vehicle details (Make, Model, and Year) using a Vehicle Identification Number (VIN). It utilizes the [API Ninjas VIN Lookup API](https://api-ninjas.com/api/vinlookup) to retrieve this information.

## Setup Instructions

1.  **Clone the Repository (Optional)**
    If you haven't already, clone the repository to your local machine:
    ```bash
    git clone https://github.com/johne3x/vin-lookup-tool
    cd vin-lookup-tool
    ```

2.  **Create a Python Virtual Environment**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```

4.  **Install Dependencies**
    Install the required Python packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Create a `.env` file**
    In the root directory of the project, create a file named `.env`.

2.  **Add API Key**
    Open the `.env` file and add your API Ninjas API key in the following format:
    ```
    API_NINJAS_KEY='YOUR_API_KEY_HERE'
    ```
    Replace `YOUR_API_KEY_HERE` with your actual API key obtained from [API Ninjas](https://api-ninjas.com/profile).

## How to Run

1.  **Execute the script:**
    Make sure your virtual environment is activated and you are in the project's root directory.
    ```bash
    python app.py
    ```

2.  **Enter VIN:**
    The application will prompt you to enter a VIN.
    ```
    Enter VIN: XXXXXXXXXXXXXXXXX
    ```
    Replace `XXXXXXXXXXXXXXXXX` with the actual VIN you want to look up.

## Example Usage

```bash
(venv) $ python app.py
Enter VIN: 123ABC456DEF789GHI
Make: Honda, Model: Civic, Year: 2023
```

If an error occurs (e.g., invalid VIN, network issue, incorrect API key), an error message will be displayed:
```bash
(venv) $ python app.py
Enter VIN: INVALIDVIN
Error: Could not retrieve data. Status code: 400
```
Or
```bash
(venv) $ python app.py
Enter VIN: 123ABC456DEF789GHI
Error: API_NINJAS_KEY not found in environment variables. Please set it in the .env file.
```
