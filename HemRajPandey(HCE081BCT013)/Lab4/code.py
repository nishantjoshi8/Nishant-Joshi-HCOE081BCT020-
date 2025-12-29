import matplotlib.pyplot as plt

# Q1: Midpoint Circle Algorithm
def midpoint_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    d = 1 - r

    while x <= y:
        # Add symmetric points (8-way symmetry)
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ])
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    return points

# Q2: Draw circles with different radii and centres
circles = [
    (0, 0, 10),     # Center at (0,0), radius 10
    (20, 20, 15),   # Center at (20,20), radius 15
    (-15, 10, 8),   # Center at (-15,10), radius 8
    (10, -20, 12)   # Center at (10,-20), radius 12
]

plt.figure(figsize=(8, 8))
for xc, yc, r in circles:
    pts = midpoint_circle(xc, yc, r)
    x, y = zip(*pts)
    plt.scatter(x, y, s=10)
plt.title("Circles with Different Radii and Centres")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()

# Q3: Concentric circles (target pattern)
plt.figure(figsize=(8, 8))
for r in range(5, 30, 5):  # radii: 5, 10, 15, 20, 25
    pts = midpoint_circle(0, 0, r)
    x, y = zip(*pts)
    plt.scatter(x, y, s=10)
plt.title("Concentric Circles (Target Pattern)")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()