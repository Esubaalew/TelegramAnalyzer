import pandas as pd
from openpyxl import Workbook
import sys
sys.path.append('../')
from tool import load_json, get_user_activity

def create_user_activity_table(data: dict, output_file: str) -> str:
    """
    Create a table or Excel file from the user activity data.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    - output_file (str): File path to save the table or Excel file.

    Returns:
    - output_file (str): File path of the saved Excel file.
    """

    user_activity = get_user_activity(data)

    
    rows = []
    for user, activity_info in user_activity.items():
        row = {'User': user}
        for time_dimension, counts in activity_info.items():
            if time_dimension != 'Overall':
                most_active_time = counts['most_active']
                most_active_count = counts['messages']
                row[f"Most active {time_dimension}"] = f"{most_active_time} (Messages: {most_active_count})"
        rows.append(row)
    
    df = pd.DataFrame(rows)

   
    df.to_excel(output_file, index=False)

    
    return output_file
