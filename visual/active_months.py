
from datetime import datetime
from matplotlib import cm
import matplotlib.pyplot as plt
import sys

import numpy as np
sys.path.append('../')
from tool import get_most_active_months, get_most_active_months_all_time, get_most_active_months_by_year, load_json

def visualize_bar_chart(data: dict):
    """
    Visualize the most active months in the Telegram group for all months and all years using a bar chart.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    
    active_months_list = get_most_active_months_all_time(data)

    
    months = [month['name'] for month in active_months_list]
    message_counts = [month['messages'] for month in active_months_list]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.bar(months, message_counts, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Message Count')
    plt.title('Most Active Months in the Telegram Group (All Time)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def visualize_line_chart(data: dict):
    """
    Visualize the most active months in the Telegram group for all months and all years using a line chart.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    
    active_months_list = get_most_active_months_all_time(data)

   
    months = [month['name'] for month in active_months_list]
    message_counts = [month['messages'] for month in active_months_list]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(months, message_counts, marker='o', color='skyblue', linestyle='-')
    plt.xlabel('Month')
    plt.ylabel('Message Count')
    plt.title('Most Active Months in the Telegram Group (All Time)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def visualize_area_chart(data: dict):
    """
    Visualize the most active months in the Telegram group for all months and all years using an area chart.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    
    active_months_list = get_most_active_months_all_time(data)

    
    months = [month['name'] for month in active_months_list]
    message_counts = [month['messages'] for month in active_months_list]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.fill_between(months, message_counts, color='skyblue', alpha=0.4)
    plt.plot(months, message_counts, color='skyblue', alpha=0.8, marker='o', linestyle='-')
    plt.xlabel('Month')
    plt.ylabel('Message Count')
    plt.title('Most Active Months in the Telegram Group (All Time)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def visualize_pie_chart(data: dict):
    """
    Visualize the most active months in the Telegram group for all months and all years using a pie chart.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    
    active_months_list = get_most_active_months_all_time(data)

    
    months = [month['name'] for month in active_months_list]
    message_counts = [month['messages'] for month in active_months_list]

    plt.figure(figsize=(8, 8))
    plt.pie(message_counts, labels=months, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Most Active Months in the Telegram Group (All Time)')
    plt.show()


def visualize_most_active_months_trend(data: dict):
   
    active_months = get_most_active_months(data)

   
    months = [datetime.strptime(month, '%Y-%m') for month, _ in active_months]
    message_counts = [count for _, count in active_months]

    # Plotting the trend using a line chart
    plt.figure(figsize=(12, 6))
    plt.plot(months, message_counts, marker='o', color='skyblue', linestyle='-')
    plt.xlabel('Month')
    plt.ylabel('Message Count')
    plt.title('Trend of Most Active Months in the Telegram Group (Monthly)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True) 
    plt.show()



def visualize_top_10_most_active_months(data: dict):
  
    active_months = get_most_active_months(data)

    # Get the top 10 most active months
    top_10_months = [month for month, _ in active_months[:10]]
    top_10_message_counts = [count for _, count in active_months[:10]]

   
    colors = cm.viridis(np.linspace(0, 1, len(top_10_months)))

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(top_10_months, top_10_message_counts, color=colors)
    ax.set_xlabel('Month')
    ax.set_ylabel('Message Count')
    ax.set_title('Top 10 Most Active Months in the Telegram Group')
    plt.xticks(rotation=45)

    # Add a color bar
    sm = plt.cm.ScalarMappable(cmap=cm.viridis, norm=plt.Normalize(vmin=0, vmax=max(top_10_message_counts)))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax) 
    cbar.set_label('Message Count')

   
    plt.tight_layout()
    plt.show()

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