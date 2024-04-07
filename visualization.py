from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from tool import get_most_active_days, get_most_active_hours, get_most_active_months_by_year, get_most_active_users, get_most_active_weekdays, get_most_active_year, load_json, get_senders, each_average_message_length

def visualize_most_active_users(data: dict, top_n: int = 10):
    """
    Visualize the top N most activ users based on the number of messages they sent.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top users to visualize. Defaults to 10.
    """

    top_active_users = get_most_active_users(data, top_n)


    users = [user['user'] for user in top_active_users]
    message_counts = [user['message_count'] for user in top_active_users]

   
    plt.figure(figsize=(10, 6))
    sns.barplot(x=message_counts, y=users, palette="viridis")
    plt.xlabel('Message Count')
    plt.ylabel('User')
    plt.title(f'Top {top_n} Most Active Users')
    plt.show()


def visualize_senders_pie(data: dict, top_n: int = 10):
    """
    Visualize the proportion of messages sent by each sender using a pie chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top senders to include. Defaults to 10.
    """
 
    senders_ranked = get_senders(data)[:top_n]

  
    senders = [sender['sender'] for sender in senders_ranked]
    message_counts = [sender['messages'] for sender in senders_ranked]

   
    plt.figure(figsize=(8, 8))
    plt.pie(message_counts, labels=senders, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    plt.title(f'Proportion of Messages Sent by Top {top_n} Senders')
    plt.axis('equal')
    plt.show()

def visualize_senders_line(data: dict, top_n: int = 10):
    """
    Visualize the number of messages sent by each sender using a line plot.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top senders to include. Defaults to 10.
    """

    senders_ranked = get_senders(data)[:top_n]

    
    senders = [sender['sender'] for sender in senders_ranked]
    message_counts = [sender['messages'] for sender in senders_ranked]

  
    plt.figure(figsize=(10, 6))
    plt.plot(senders, message_counts, marker='o', linestyle='-', color='b')
    plt.xlabel('Sender')
    plt.ylabel('Number of Messages')
    plt.title(f'Number of Messages Sent by Top {top_n} Senders')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def visualize_senders_scatter(data: dict, top_n: int = 10):
    """
    Visualize the number of messages sent by each sender using a scatter plot.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top senders to include. Defaults to 10.
    """
   
    senders_ranked = get_senders(data)[:top_n]

    
    senders = [sender['sender'] for sender in senders_ranked]
    message_counts = [sender['messages'] for sender in senders_ranked]

  
    plt.figure(figsize=(10, 6))
    plt.scatter(senders, message_counts, color='b', alpha=0.7)
    plt.xlabel('Sender')
    plt.ylabel('Number of Messages')
    plt.title(f'Number of Messages Sent by Top {top_n} Senders')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def visualize_average_message_length(data: dict, top_n: int = 10):
    """
    Visualize the average message length for each user using a bar chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top users to include. Defaults to 10.
    """
   
    average_lengths = each_average_message_length(data)

    
    sorted_users = sorted(average_lengths.items(), key=lambda x: x[1], reverse=True)[:top_n]

    
    users = [user[0] for user in sorted_users]
    lengths = [user[1] for user in sorted_users]

  
    plt.figure(figsize=(10, 6))
    plt.barh(users, lengths, color='skyblue')
    plt.xlabel('Average Message Length')
    plt.ylabel('User')
    plt.title(f'Top {top_n} Users by Average Message Length')
    plt.gca().invert_yaxis() 
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def visualize_most_active_hours(data: dict):
    """
    Visualize the most active hours in the Telegram group using a histogram with different colors.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
  
    active_hours = get_most_active_hours(data)

    
    hours = [hour for hour, count in active_hours]
    counts = [count for hour, count in active_hours]

    
    colormap = plt.cm.viridis  

   
    min_count = min(counts)
    max_count = max(counts)
    normalized_counts = [(count - min_count) / (max_count - min_count) for count in counts]

    
    plt.figure(figsize=(10, 6))
    for hour, count, normalized_count in zip(hours, counts, normalized_counts):
        color = colormap(normalized_count) 
        plt.bar(hour, count, color=color)

    plt.xlabel('Hour of Day')
    plt.ylabel('Message Count')
    plt.title('Most Active Hours in the Telegram Group')
    plt.xticks(range(24))  
    plt.grid(axis='y', linestyle='--', alpha=0.7)

  
    sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=min_count, vmax=max_count))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=plt.gca()) 
    cbar.set_label('Message Count')

    plt.show()


def visualize_activity_over_time(data: dict):
    """
    Visualize the change in activity over time from the oldest day to the newest day using a line plot.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
 
    active_days = get_most_active_days(data)

   
    days = [datetime.strptime(day, '%Y-%m-%d') for day, count in active_days]
    counts = [count for day, count in active_days]

    # Plot the line plot
    plt.figure(figsize=(12, 6))
    plt.plot(days, counts, marker='o', linestyle='-')

    plt.xlabel('Date')
    plt.ylabel('Message Count')
    plt.title('Change in Activity Over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def visualize_most_active_weekdays_pie(data: dict):
    """
    Visualize the distribution of message activity across different weekdays using a pie chart.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
   
    active_weekdays = get_most_active_weekdays(data)

   
    weekdays = [day for day, count in active_weekdays]
    counts = [count for day, count in active_weekdays]

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=weekdays, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
    plt.title('Distribution of Message Activity Across Weekdays')
    plt.axis('equal') 

    plt.show()


def visualize_message_activity_over_year(data: dict):
    """
    Visualize the change in message activity over time using a line plot.

    Args:
    - data (dict): The JSON data from the Telegram group export.
    """
    active_years_data = get_most_active_year(data)
   
    sorted_years = sorted(active_years_data)
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