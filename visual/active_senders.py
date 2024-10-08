
from matplotlib import pyplot as plt
import seaborn as sns
import sys
sys.path.append('../')
from tool import get_most_active_users, get_senders, load_json


def visualize_bar_chart(data: dict, top_n: int = 10):
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


def visualize_pie_chart(data: dict, top_n: int = 10):
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

def visualize_Vbar_chart(data: dict, top_n: int = 10):
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
    sns.barplot(x=users, y=message_counts, palette="viridis")
    plt.xlabel('Message Count')
    plt.ylabel('User')
    plt.title(f'Top {top_n} Most Active Users')
    plt.show()


def visualize_line__chart(data: dict, top_n: int = 10):
    """
    Visualize the top N most active users based on the number of messages they sent using a line chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top users to visualize. Defaults to 10.
    """

    top_active_users = get_most_active_users(data, top_n)

    users = [user['user'] for user in top_active_users]
    message_counts = [user['message_count'] for user in top_active_users]

    plt.figure(figsize=(10, 6))
    plt.plot(users, message_counts, marker='o', color='skyblue', linestyle='-')
    plt.xlabel('User')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Most Active Users (Line Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def visualize__area_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N most active users based on the number of messages they sent using an area chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top users to visualize. Defaults to 10.
    """

    top_active_users = get_most_active_users(data, top_n)

    users = [user['user'] for user in top_active_users]
    message_counts = [user['message_count'] for user in top_active_users]

    plt.figure(figsize=(10, 6))
    plt.fill_between(users, message_counts, color='skyblue', alpha=0.4)
    plt.plot(users, message_counts, color='skyblue', alpha=0.8, marker='o', linestyle='-')
    plt.xlabel('User')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Most Active Users (Area Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()