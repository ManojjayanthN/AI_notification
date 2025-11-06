from datetime import datetime

def parse_datetime(dt_string):
    """Convert string to datetime object"""
    return datetime.strptime(dt_string, "%Y-%m-%d %H:%M")

def format_datetime(dt_obj):
    """Convert datetime object to readable string"""
    return dt_obj.strftime("%d-%m-%Y %H:%M")
