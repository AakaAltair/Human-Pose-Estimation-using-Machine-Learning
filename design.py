from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

def draw_diagram():
    fig, ax = plt.subplots(figsize=(10, 7))

    # Define key stages as rectangles
    stages = [
        {"name": "Input Stage", "x": 0, "y": 3, "text": "Input Video/Image\n(Recorded or Live)", "color": "skyblue"},
        {"name": "Preprocessing", "x": 2, "y": 3, "text": "Preprocessing\n(Resize, Normalize)", "color": "lightgreen"},
        {"name": "Pose Estimation Model", "x": 4, "y": 3, "text": "Pose Estimation\nModel (e.g., MediaPipe)", "color": "lightcoral"},
        {"name": "Postprocessing", "x": 6, "y": 3, "text": "Postprocessing\n(Landmark Processing)", "color": "gold"},
        {"name": "Application-Specific Module", "x": 8, "y": 3, "text": "Application\n(Motion Analysis)", "color": "plum"},
        {"name": "Output Stage", "x": 10, "y": 3, "text": "Output Results\n(Annotated Frames)", "color": "deepskyblue"},
    ]

    # Draw rectangles
    for stage in stages:
        rect = mpatches.Rectangle((stage['x'], stage['y']), 1.8, 1, color=stage['color'], ec="black")
        ax.add_patch(rect)
        ax.text(stage['x'] + 0.9, stage['y'] + 0.5, stage['text'], ha='center', va='center', fontsize=10)

    # Draw arrows
    for i in range(len(stages) - 1):
        ax.arrow(stages[i]['x'] + 1.8, stages[i]['y'] + 0.5, 0.4, 0, head_width=0.2, head_length=0.2, fc='black', ec='black')

    # Set limits and remove axes
    ax.set_xlim(-1, 12)
    ax.set_ylim(2, 5)
    ax.axis('off')

    # Title
    plt.title("Proposed System Design for Human Pose Estimation", fontsize=14, weight="bold")
    plt.show()

draw_diagram()