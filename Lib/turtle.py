import matplotlib.pyplot as plt
import numpy as np

def draw_heart_with_text():
    # Create heart shape using parametric equations
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    # Plot the heart shape
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color='red', linewidth=2)
    plt.fill(x, y, color='red', alpha=0.8)

    # Add text in the middle
    plt.text(0, -2, 'I Love You', fontsize=20, fontweight='bold', color='white',
             ha='center', va='center')

    # Adjust plot settings
    plt.axis('off')  # Turn off axes
    plt.gca().set_aspect('equal', adjustable='box')  # Keep aspect ratio equal

    # Show the plot
    plt.show()

# Call the function to draw the heart with text
draw_heart_with_text()
