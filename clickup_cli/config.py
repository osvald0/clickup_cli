import os
from dotenv import load_dotenv
from clickup_cli.types import ClickupConfig


def get_config() -> ClickupConfig:
    """
    Load configuration from environment variables or .env file and validate required keys.
    """
    load_dotenv()

    config = {
        "CLICKUP_API_TOKEN": os.getenv("CLICKUP_API_TOKEN"),
        "CLICKUP_TEAM_ID": os.getenv("CLICKUP_TEAM_ID"),
        "CLICKUP_USER_ID": os.getenv("CLICKUP_USER_ID"),
    }

    missing_keys = [key for key, value in config.items() if not value]

    if missing_keys:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_keys)}. "
            "Please check your .env file or environment variables."
        )

    return config
