from matplotlib import pyplot as plt
import seaborn as sns
import sys
sys.path.append('../')
from tool import get_forward_sources, load_json


def visualize_bar_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forward sources based on the number of messages they forwarded.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forward sources to visualize. Defaults to 10.
    """

    # Get forward sources data
    forward_source_ranking = get_forward_sources(data)
    top_forward_sources = list(forward_source_ranking.keys())[:top_n]
    message_counts = list(forward_source_ranking.values())[:top_n]

    # Create bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=message_counts, y=top_forward_sources, palette="viridis")
    plt.xlabel('Message Count')
    plt.ylabel('Forward Source')
    plt.title(f'Top {top_n} Forward Sources by Message Count')
    plt.show()


def visualize_pie_chart(data: dict, top_n: int = 6):
    """
    Visualize the proportion of messages forwarded by each forward source using a pie chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forward sources to include. Defaults to 6.
    """
    forward_source_ranking = get_forward_sources(data)
    top_forward_sources = list(forward_source_ranking.keys())[:top_n]
    message_counts = list(forward_source_ranking.values())[:top_n]

    plt.figure(figsize=(8, 8))
    plt.pie(message_counts, labels=top_forward_sources, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    plt.title(f'Proportion of Messages Forwarded by Top {top_n} Forward Sources')
    plt.axis('equal')
    plt.show()


def visualize_vertical_bar_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forward sources based on the number of messages they forwarded.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forward sources to visualize. Defaults to 10.
    """

    forward_source_ranking = get_forward_sources(data)
    top_forward_sources = list(forward_source_ranking.keys())[:top_n]
    message_counts = list(forward_source_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_forward_sources, y=message_counts, palette="viridis")
    plt.xlabel('Forward Source')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Forward Sources by Message Count')
    plt.show()


def visualize_line_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forward sources based on the number of messages they forwarded using a line chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forward sources to visualize. Defaults to 10.
    """

    forward_source_ranking = get_forward_sources(data)
    top_forward_sources = list(forward_source_ranking.keys())[:top_n]
    message_counts = list(forward_source_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    plt.plot(top_forward_sources, message_counts, marker='o', color='skyblue', linestyle='-')
    plt.xlabel('Forward Source')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Forward Sources (Line Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def visualize_area_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N forward sources based on the number of messages they forwarded using an area chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top forward sources to visualize. Defaults to 10.
    """

    forward_source_ranking = get_forward_sources(data)
    top_forward_sources = list(forward_source_ranking.keys())[:top_n]
    message_counts = list(forward_source_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    plt.fill_between(top_forward_sources, message_counts, color='skyblue', alpha=0.4)
    plt.plot(top_forward_sources, message_counts, color='skyblue', alpha=0.8, marker='o', linestyle='-')
    plt.xlabel('Forward Source')
    plt.ylabel('Message Count')
    plt.title(f'Top {top_n} Forward Sources (Area Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()
