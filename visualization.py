from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from tool import get_most_active_days, get_most_active_hours, get_most_active_months_all_time, get_most_active_months_by_year, get_most_active_users, get_most_active_weekdays, get_most_active_year, load_json, get_senders, each_average_message_length



def visualize_most_active_months_by_year(data: dict):
    """
    Visualize the most active months in the Telegram group for each year using a grouped bar plot and export the data.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    - export_excel (bool): Whether to export the data to an Excel file. Defaults to True.
    - export_json (bool): Whether to export the data to a JSON file. Defaults to True.
    """
   
    active_months_by_year = get_most_active_months_by_year(data)

    
    years = sorted(active_months_by_year.keys())
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    num_months = len(month_names)
    bar_width = 0.35
    index = np.arange(num_months)

    
    for year, months_data in active_months_by_year.items():
        if len(months_data) < num_months:
            missing_months = set(month_names) - set(month['name'] for month in months_data)
            for month in missing_months:
                active_months_by_year[year].append({'name': month, 'messages': 0})
        active_months_by_year[year] = sorted(active_months_by_year[year], key=lambda x: month_names.index(x['name']))

    
    plt.figure(figsize=(12, 8))

    for i, year in enumerate(years):
        months_data = active_months_by_year[year]
        month_counts = [month['messages'] for month in months_data]
        plt.bar(index + i * bar_width, month_counts, bar_width, label=year)

    plt.xlabel('Month')
    plt.ylabel('Message Count')
    plt.title('Most Active Months by Year')
    plt.xticks(index + bar_width * len(years) / 2, month_names)
    plt.legend(title='Year')
    plt.tight_layout()
    plt.show()


data = load_json(r'D:\PlayingWithPython\TelegramAnalyzer\result.json')

visualize_most_active_months_by_year(data)
