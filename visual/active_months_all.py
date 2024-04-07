
from datetime import datetime
from matplotlib import cm
import matplotlib.pyplot as plt
import sys

import numpy as np
sys.path.append('../')
from tool import get_most_active_months, get_most_active_months_all_time, load_json

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

# Example usage
data = load_json(r'D:\PlayingWithPython\TelegramAnalyzer\result.json')
# visualize_bar_chart(data)
# visualize_line_chart(data)
# visualize_area_chart(data)
# visualize_pie_chart(data)
# visualize_most_active_months_trend(data)
# visualize_top_10_most_active_months(data)