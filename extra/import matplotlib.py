import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title("Earth with No Gravity")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Create multiple objects (e.g., floating particles)
num_objects = 20
objects = [{'x': random.uniform(10, 90), 
            'y': random.uniform(10, 90), 
            'dx': random.uniform(-1, 1), 
            'dy': random.uniform(-1, 1)} for _ in range(num_objects)]

# Plot objects
scatter = ax.scatter([obj['x'] for obj in objects], [obj['y'] for obj in objects])

def update(frame):
    global objects
    for obj in objects:
        # Update positions
        obj['x'] += obj['dx']
        obj['y'] += obj['dy']
        
        # Keep objects within bounds (simulate wrapping around Earth)
        obj['x'] = obj['x'] % 100
        obj['y'] = obj['y'] % 100

    # Update scatter plot data
    scatter.set_offsets([[obj['x'], obj['y']] for obj in objects])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
