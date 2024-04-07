import sys

from matplotlib import pyplot as plt
sys.path.append('../')
from tool import  get_most_active_weekdays, load_json


def visualize_most_active_weekdays_bar(data: dict):
    active_weekdays = get_most_active_weekdays(data)

    weekdays = [weekday for weekday, _ in active_weekdays]
    message_counts = [count for _, count in active_weekdays]

    plt.figure(figsize=(10, 6))
    plt.bar(weekdays, message_counts, color='skyblue')
    plt.xlabel('Weekday')
    plt.ylabel('Message Count')
    plt.title('Most Active Weekdays in the Telegram Group')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_most_active_weekdays_pie(data: dict):
    active_weekdays = get_most_active_weekdays(data)

    weekdays = [weekday for weekday, _ in active_weekdays]
    message_counts = [count for _, count in active_weekdays]

    plt.figure(figsize=(8, 8))
    plt.pie(message_counts, labels=weekdays, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Most Active Weekdays in the Telegram Group')
    plt.show()

data = load_json(r'D:\PlayingWithPython\TelegramAnalyzer\result.json')
# visualize_most_active_weekdays_bar(data)
# visualize_most_active_weekdays_pie(data)