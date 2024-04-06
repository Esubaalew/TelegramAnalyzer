import matplotlib.pyplot as plt
import seaborn as sns
from tool import get_most_active_users, load_json, get_senders

def visualize_most_active_users(data: dict, top_n: int = 10):
    """
    Visualize the top N most active users based on the number of messages they sent.

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