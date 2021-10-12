"""Time action implementation."""

import datetime as dt

import pytz


def get_current_time(location: str) -> str:
    """Get current time in `location`.

    Args:
        location: Europe/Moscow, Asia/Irkutsk, etc.

    Returns:
        current time in `location`
    """
    time_format = '%H:%M:%S'
    location_timezone = pytz.timezone(location)
    current_datetime = dt.datetime.now().astimezone(location_timezone)
    return current_datetime.strftime(time_format)
