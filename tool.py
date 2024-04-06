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