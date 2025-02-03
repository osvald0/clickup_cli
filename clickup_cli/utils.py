from datetime import datetime


def format_date(timestamp) -> str:
    """
    Convert a Unix timestamp to a human-readable date.
    """
    if not timestamp:
        return "No due date"
    return datetime.fromtimestamp(int(timestamp) / 1000).strftime("%Y-%m-%d %H:%M:%S")


def hex_to_ansi(hex_color, text):
    """
    Convert color from hex to ansi and assign it to a text.
    """
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def convert_ms_to_hm(milliseconds):
    """
    Convert milliseconds into hours (H) and minutes (M).
    """
    if milliseconds <= 0:
        return "0H"  # Handle zero or negative values gracefully

    total_minutes = milliseconds // 60000  # Convert to minutes
    hours = total_minutes // 60  # Get whole hours
    minutes = total_minutes % 60  # Get remaining minutes

    if hours > 0 and minutes > 0:
        return f"{hours}H {minutes}M"
    elif hours > 0:
        return f"{hours}H"
    else:
        return f"{minutes}M"
