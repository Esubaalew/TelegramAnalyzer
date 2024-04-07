from matplotlib import pyplot as plt
import seaborn as sns
import sys
sys.path.append('../')
from tool import get_most_active_year, load_json



def visualize_message_trend_over_year(data: dict):
    """
    Visualize the change in message activity over time using a line plot.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    active_years_data = get_most_active_year(data)
   
    sorted_years = active_years_data
    years, message_counts = zip(*sorted_years)


    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(years, message_counts, marker='o')
    plt.title('Number of Messages Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Messages')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_message_trend_over_year_bar(data: dict):
    """
    Visualize the change in message activity over time using a bar chart.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    active_years_data = get_most_active_year(data)
   
    sorted_years = active_years_data
    years, message_counts = zip(*sorted_years)

    # Plotting bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(years, message_counts, color='skyblue')
    plt.title('Number of Messages Over Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Messages')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_message_trend_over_year_pie(data: dict):
    """
    Visualize the distribution of message activity over years using a pie chart.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    active_years_data = get_most_active_year(data)
   
    sorted_years = active_years_data
    years, message_counts = zip(*sorted_years)

    # Plotting pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(message_counts, labels=years, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Message Distribution Over Years')
    plt.show()