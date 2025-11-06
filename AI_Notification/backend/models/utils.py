from datetime import datetime

def parse_datetime(dt_string):
    return datetime.strptime(dt_string, "%Y-%m-%d %H:%M")

def format_datetime(dt_obj):
    return dt_obj.strftime("%d-%m-%Y %H:%M")
