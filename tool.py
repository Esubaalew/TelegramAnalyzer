import json

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