from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import seaborn as sns
import sys
sys.path.append('../')
from tool import get_most_active_hours, load_json

def visualize_bar(data: dict):
   
    active_hours = get_most_active_hours(data)
    hours, counts = zip(*active_hours)

    # Convert UTC to Ethiopian time
    ethiopian_hours = [(datetime.strptime(str(hour), '%H') + timedelta(hours=3)).strftime('%I %p') for hour in hours]

    
    colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'yellow', 'brown', 'pink', 'gray', 'cyan', 'magenta', 'lightgreen']

    # Plotting the bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(ethiopian_hours, counts, color=colors)
    plt.xlabel('Hour of the Day (Ethiopian Time)')
    plt.ylabel('Message Count')
    plt.title('Most Active Hours in the Telegram Group')
    plt.grid(axis='y', linestyle='--', alpha=0.7) 
    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()


def visualize_line(data: dict):
    
    active_hours = get_most_active_hours(data)
    hours, counts = zip(*active_hours)

    # Convert UTC to Ethiopian time
    ethiopian_hours = [(datetime.strptime(str(hour), '%H') + timedelta(hours=3)).strftime('%I %p') for hour in hours]

    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(ethiopian_hours, counts, marker='o', color='skyblue', linestyle='-')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Message Count')
    plt.title('Most Active Hours in the Telegram Group')
    plt.xticks(range(24))  
    plt.grid(True, linestyle='--', alpha=0.7) 
    plt.show()