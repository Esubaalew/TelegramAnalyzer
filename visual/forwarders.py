from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import sys
sys.path.append('../')
from tool import get_forwarders, load_json


def visualize_bar_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forwarders based on the number of messages they forwarded.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forwarders to visualize. Defaults to 10.
    """

    # Get forwarders data
    forwarder_ranking = get_forwarders(data)
    top_forwarders = list(forwarder_ranking.keys())[:top_n]
    message_counts = list(forwarder_ranking.values())[:top_n]

    # Create bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=message_counts, y=top_forwarders, palette="viridis")
    plt.xlabel('Message Count')
    plt.ylabel('Forwarder')
    plt.title(f'Top {top_n} Forwarders by Message Count')
    plt.show()


def visualize_pie_chart(data: dict, top_n: int = 6):
    """
    Visualize the proportion of messages forwarded by each forwarder using a pie chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forwarders to include. Defaults to 10.
    """
    forwarder_ranking = get_forwarders(data)
    top_forwarders = list(forwarder_ranking.keys())[:top_n]
    message_counts = list(forwarder_ranking.values())[:top_n]

    plt.figure(figsize=(8, 8))
    plt.pie(message_counts, labels=top_forwarders, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    plt.title(f'Proportion of Messages Forwarded by Top {top_n} Forwarders')
    plt.axis('equal')
    plt.show()


def visualize_vertical_bar_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forwarders based on the number of messages they forwarded.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forwarders to visualize. Defaults to 10.
    """

    forwarder_ranking = get_forwarders(data)
    top_forwarders = list(forwarder_ranking.keys())[:top_n]
    message_counts = list(forwarder_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_forwarders, y=message_counts, palette="viridis")
    plt.xlabel('Forwarder')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Forwarders by Message Count')
    plt.show()


def visualize_line_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forwarders based on the number of messages they forwarded using a line chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forwarders to visualize. Defaults to 10.
    """

    forwarder_ranking = get_forwarders(data)
    top_forwarders = list(forwarder_ranking.keys())[:top_n]
    message_counts = list(forwarder_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    plt.plot(top_forwarders, message_counts, marker='o', color='skyblue', linestyle='-')
    plt.xlabel('Forwarder')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Forwarders (Line Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def visualize_area_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forwarders based on the number of messages they forwarded using an area chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forwarders to visualize. Defaults to 10.
    """

    forwarder_ranking = get_forwarders(data)
    top_forwarders = list(forwarder_ranking.keys())[:top_n]
    message_counts = list(forwarder_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    plt.fill_between(top_forwarders, message_counts, color='skyblue', alpha=0.4)
    plt.plot(top_forwarders, message_counts, color='skyblue', alpha=0.8, marker='o', linestyle='-')
    plt.xlabel('Forwarder')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Forwarders (Area Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


# Example usage
data = load_json(r'D:\PlayingWithPython\TelegramAnalyzer\result.json')
# visualize_bar_chart(data, top_n=10)
# visualize_pie_chart(data, top_n=6)
# visualize_line_chart(data, top_n=10)
# visualize_area_chart(data, top_n=10)
# visualize_vertical_bar_chart(data, top_n=10)
