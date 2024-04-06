import json
from datetime import datetime

def load_json(file_path: str = 'result.json') -> dict:
    """
    Load JSON data from the specified file path.

    Args:
    - file_path (str): The path to the JSON file.

    Returns:
    - data (dict): The loaded JSON data.
    - None: If an error occurs during file opening or JSON parsing.
    """
    try:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"An error occurred while loading the JSON file: {e}")
        return None


def chat_info(data: dict) -> dict:
    """
    Extract chat information from the JSON data.

    Args:
    - data (dict): The JSON data.

    Returns:
    - chat_info (dict): Dictionary containing chat information.
    """
    chat = data
    messages_count = len(data.get('messages', []))

    chat_info = {
        'name': chat.get('name', 'Unknown'),
        'type': chat.get('type', 'Unknown'),
        'id': chat.get('id', 'Unknown'),
        'messages_count': messages_count
    }

    return chat_info

def get_oldest_message(data: dict) -> dict:
    """
    Retrieves the oldest message from the JSON data.

    Args:
    - data (dict): The JSON data.

    Returns:
    - oldest_message (dict): Dictionary containing the oldest message with full timestamp.
    """
    
    oldest_message = {'date': '9999-12-31T23:59:59'}
    
    for message in data.get('messages', []):
        if 'date' in message and message['date'] < oldest_message['date']:
            oldest_message = message

    oldest_message['date'] = extract_date_info(oldest_message)

    return oldest_message


def extract_date_info(message: dict) -> dict:
    """
    Extract date information from the message and return it as a dictionary.

    Args:
    - message (dict): The message containing the date information.

    Returns:
    - date_info (dict): Dictionary containing the extracted date information.
    """
    date_str = message.get('date')
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

    date_info = {
        'year': date_obj.year,
        'month': date_obj.month,
        'day': date_obj.day,
        'hour': date_obj.hour,
        'minute': date_obj.minute,
        'second': date_obj.second,
        'time': date_obj.strftime('%H:%M:%S')
    }

    return date_info
