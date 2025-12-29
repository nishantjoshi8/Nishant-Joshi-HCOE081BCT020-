import matplotlib.pyplot as plt

# Q1: Implement Bresenham’s Algorithm
def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

# DDA Algorithm
def dda(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return points

# Q2: Draw lines for different octants and compare visually
octant_lines = [
    (0, 0, 10, 5),   # Octant 1
    (0, 0, 5, 10),   # Octant 2
    (0, 0, -5, 10),  # Octant 3
    (0, 0, -10, 5),  # Octant 4
    (0, 0, -10, -5), # Octant 5
    (0, 0, -5, -10), # Octant 6
    (0, 0, 5, -10),  # Octant 7
    (0, 0, 10, -5)   # Octant 8
]

plt.figure(figsize=(12, 12))
for i, (x1, y1, x2, y2) in enumerate(octant_lines, 1):
    bres_points = bresenham(x1, y1, x2, y2)
    dda_points = dda(x1, y1, x2, y2)

    plt.subplot(3, 3, i)
    bx, by = zip(*bres_points)
    dx, dy = zip(*dda_points)
    plt.plot(bx, by, 'ro-', label="Bresenham")
    plt.plot(dx, dy, 'bo-', label="DDA")
    plt.title(f"Octant {i}")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()