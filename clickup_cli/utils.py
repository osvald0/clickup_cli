from datetime import datetime

def format_date(timestamp):
    """
    Convert a Unix timestamp to a human-readable date.
    """
    if not timestamp:
        return "No due date"
    return datetime.fromtimestamp(int(timestamp) / 1000).strftime('%Y-%m-%d %H:%M:%S')
