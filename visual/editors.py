from matplotlib import pyplot as plt
import seaborn as sns
import sys
sys.path.append('../')
from tool import get_editors, load_json


def visualize_bar_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N editors based on the number of edited messages.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top editors to visualize. Defaults to 10.
    """

    # Get editors data
    editor_ranking = get_editors(data)
    top_editors = list(editor_ranking.keys())[:top_n]
    edited_message_counts = list(editor_ranking.values())[:top_n]

    # Create bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=edited_message_counts, y=top_editors, palette="viridis")
    plt.xlabel('Edited Message Count')
    plt.ylabel('Editor')
    plt.title(f'Top {top_n} Editors by Edited Message Count')
    plt.show()


def visualize_pie_chart(data: dict, top_n: int = 6):
    """
    Visualize the proportion of edited messages by each editor using a pie chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top editors to include. Defaults to 6.
    """
    editor_ranking = get_editors(data)
    top_editors = list(editor_ranking.keys())[:top_n]
    edited_message_counts = list(editor_ranking.values())[:top_n]

    plt.figure(figsize=(8, 8))
    plt.pie(edited_message_counts, labels=top_editors, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    plt.title(f'Proportion of Edited Messages by Top {top_n} Editors')
    plt.axis('equal')
    plt.show()


def visualize_vertical_bar_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N editors based on the number of edited messages.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top editors to visualize. Defaults to 10.
    """

    editor_ranking = get_editors(data)
    top_editors = list(editor_ranking.keys())[:top_n]
    edited_message_counts = list(editor_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_editors, y=edited_message_counts, palette="viridis")
    plt.xlabel('Editor')
    plt.ylabel('Edited Message Count')
    plt.title(f'Top {top_n} Editors by Edited Message Count')
    plt.show()


def visualize_line_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N editors based on the number of edited messages using a line chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top editors to visualize. Defaults to 10.
    """

    editor_ranking = get_editors(data)
    top_editors = list(editor_ranking.keys())[:top_n]
    edited_message_counts = list(editor_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    plt.plot(top_editors, edited_message_counts, marker='o', color='skyblue', linestyle='-')
    plt.xlabel('Editor')
    plt.ylabel('Edited Message Count')
    plt.title(f'Top {top_n} Editors (Line Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def visualize_area_chart(data: dict, top_n: int = 10):
    """
    Visualize the top N editors based on the number of edited messages using an area chart.

    Args:
    - data (dict): The JSON data.
    - top_n (int): The number of top editors to visualize. Defaults to 10.
    """

    editor_ranking = get_editors(data)
    top_editors = list(editor_ranking.keys())[:top_n]
    edited_message_counts = list(editor_ranking.values())[:top_n]

    plt.figure(figsize=(10, 6))
    plt.fill_between(top_editors, edited_message_counts, color='skyblue', alpha=0.4)
    plt.plot(top_editors, edited_message_counts, color='skyblue', alpha=0.8, marker='o', linestyle='-')
    plt.xlabel('Editor')
    plt.ylabel('Edited Message Count')
    plt.title(f'Top {top_n} Editors (Area Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

