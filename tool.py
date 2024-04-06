import json
from datetime import datetime
from collections import defaultdict

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

def get_latest_message(data: dict) -> dict:
    """
    Retrieves the latest message from the JSON data.

    Args:
    - data (dict): The JSON data.

    Returns:
    - latest_message (dict): Dictionary containing the latest message with full timestamp.
    """
    latest_message = {'date': '0000-01-01T00:00:00'}
    

    for message in data.get('messages', []):
        if 'date' in message and message['date'] > latest_message['date']:
            latest_message = message

    latest_message['date'] = extract_date_info(latest_message)
    return latest_message


def get_senders_list(data: dict) -> list:
    """
    Extracts the list of unique senders from the JSON data.

    Args:
    - data (dict): The JSON data.

    Returns:
    - senders_list (list): List of unique senders.
    """
    
    unique_senders = set()


    for message in data.get('messages', []):
        sender_id = message.get('from')
        unique_senders.add(sender_id)


    senders_list = ['Deleted Account' if sender is None else sender for sender in unique_senders]

    return senders_list

def count_forwarded_messages(data: dict) -> int:
    """
    Count the number of forwarded messages in the provided JSON data.

    Args:
    - data (dict): The JSON data.

    Returns:
    - count (int): The number of forwarded messages.
    """
    count = 0
    for message in data.get('messages', []):
        if 'forwarded_from' in message:
            count += 1
    return count

def get_forwarded_messages(data: dict) -> list:
    """
    Extract all forwarded messages from the provided JSON data.

    Args:
    - data (dict): The JSON data.

    Returns:
    - forwarded_messages (list): List of dictionaries containing forwarded messages.
    """
    forwarded_messages = []
    for message in data.get('messages', []):
        if 'forwarded_from' in message:
            forwarded_messages.append(message)
    return forwarded_messages


from collections import defaultdict

def get_forwarders(data: dict) -> dict:
    """
    Get a ranking of forwarders based on the number of messages they forwarded.

    Args:
    - data (dict): The JSON data.

    Returns:
    - forwarder_ranking (dict): Dictionary containing forwarders ranked by the number of messages they forwarded.
    """
    forwarder_count = defaultdict(int)

    for message in data.get('messages', []):
        if 'forwarded_from' in message:
            forwarder = message['from']
            forwarder_count[forwarder] += 1

    forwarder_ranking = dict(sorted(forwarder_count.items(), key=lambda x: x[1], reverse=True))
    return forwarder_ranking

def get_forward_sources(data: dict) -> dict:
    """
    Get a dictionary of users (forward sources) with the number of messages they are the source for,
    sorted from largest to smallest based on the number of messages.

    Args:
    - data (dict): The JSON data.

    Returns:
    - forward_sources_count (dict): Dictionary of users with the number of messages they are the source for,
                                    sorted from largest to smallest based on the number of messages.
    """
    forward_sources_count = defaultdict(int)

    for message in data.get('messages', []):
        if 'forwarded_from' in message:
            forward_source = message['forwarded_from']
            forward_sources_count[forward_source] += 1

    
    sorted_forward_sources_count = dict(sorted(forward_sources_count.items(), key=lambda x: x[1], reverse=True))

    return sorted_forward_sources_count


def count_replies(data: dict) -> int:
    """
    Count all replies in the JSON data.

    Args:
    - data (dict): The JSON data.

    Returns:
    - reply_count (int): The total number of replies.
    """
    reply_count = 0

    for message in data.get('messages', []):
        if 'reply_to_message_id' in message:
            reply_count += 1

    return reply_count
