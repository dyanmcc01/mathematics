def calculate_pi(n):
    # Monte Carlo method to estimate pi
    inside = 0
    outside = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside += 1
        else:
            outside += 1
    return 4 * inside / n
