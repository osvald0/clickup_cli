import requests
from clickup_cli.config import get_config

API_BASE_URL = "https://api.clickup.com/api/v2"


def make_request(endpoint, params=None):
    """
    Make a request to the ClickUp API.
    """
    config = get_config()
    headers = {
        "Authorization": config["CLICKUP_API_TOKEN"],
    }
    response = requests.get(
        f"{API_BASE_URL}/{endpoint}", headers=headers, params=params
    )
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API request failed: {response.status_code}")
        print(response.json())
        return None
