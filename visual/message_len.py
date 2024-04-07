from matplotlib import pyplot as plt
import seaborn as sns
import sys
sys.path.append('../')
from tool import each_average_message_length, load_json

def visualize_bar_chart(data: dict):
    """
    Visualize the average message length for each user using a bar chart.

    Args:
    - data (dict): The JSON data.
    """

    average_lengths = each_average_message_length(data)
    users = list(average_lengths.keys())
    lengths = list(average_lengths.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=users, y=lengths, palette="viridis")
    plt.xlabel('User')
    plt.ylabel('Average Message Length')
    plt.title('Average Message Length for Each User (Bar Chart)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def visualize_horizontal_bar(data: dict):
    """
    Visualize the average message length for each user using a horizontal bar chart.

    Args:
    - data (dict): The JSON data.
    """

    average_lengths = each_average_message_length(data)
    users = list(average_lengths.keys())
    lengths = list(average_lengths.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=lengths, y=users, palette="viridis")
    plt.xlabel('Average Message Length')
    plt.ylabel('User')
    plt.title('Average Message Length for Each User (Horizontal Bar Chart)')
    plt.tight_layout()
    plt.show()


def visualize_histogram(data: dict):
    """
    Visualize the distribution of average message length for each user using a histogram.

    Args:
    - data (dict): The JSON data.
    """

    average_lengths = each_average_message_length(data)
    lengths = list(average_lengths.values())

    plt.figure(figsize=(10, 6))
    sns.histplot(lengths, bins=20, color='skyblue')
    plt.xlabel('Average Message Length')
    plt.ylabel('Frequency')
    plt.title('Distribution of Average Message Length for Each User (Histogram)')
    plt.tight_layout()
    plt.show()

data = load_json(r'D:\PlayingWithPython\TelegramAnalyzer\result.json')
# visualize_bar_chart(data)
# visualize_orizontal_bar(data)
# visualize_histogram(data)
