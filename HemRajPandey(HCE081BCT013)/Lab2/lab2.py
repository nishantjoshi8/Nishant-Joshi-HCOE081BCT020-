import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    points = []
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return points

# --- Task 1: Rectangle ---
def draw_rectangle(x1, y1, x2, y2):
    lines = []
    lines += dda_line(x1, y1, x2, y1)   # bottom
    lines += dda_line(x2, y1, x2, y2)   # right
    lines += dda_line(x2, y2, x1, y2)   # top
    lines += dda_line(x1, y2, x1, y1)   # left
    return lines

# --- Task 2: Axes ---
def draw_axes(length):
    lines = []
    lines += dda_line(-length, 0, length, 0)  # X-axis
    lines += dda_line(0, -length, 0, length)  # Y-axis
    return lines

# --- Main Program ---
rect_points = draw_rectangle(20, 20, 100, 80)
axes_points = draw_axes(150)

# Plotting
plt.figure(figsize=(6,6))
for (x,y) in rect_points:
    plt.plot(x, y, 'bo', markersize=2)
for (x,y) in axes_points:
    plt.plot(x, y, 'ro', markersize=2)

plt.title("Lab 2: DDA Rectangle and Axes")
plt.grid(True)
plt.show()