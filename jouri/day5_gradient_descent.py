x = 0

for step in range(10):
    error = (x - 3) ** 2
    print("Step:", step)
    print("x =", x)
    print("Error =", error)
    print("----------------")

    if x < 3:
        x += 0.5