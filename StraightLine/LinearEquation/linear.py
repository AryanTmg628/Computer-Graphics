"""
A program to find the coordinates to draw a line in the computer
"""


def find_slope(x1: float, x2: float, y1: float, y2: float) -> float:
    """
    Finds and returns the slope of the line
    """

    delta_y: float = y2 - y1
    delta_x: float = x2 - x1

    return delta_y / delta_x


def find_y_intercept(m: float, x1: float, y1: float) -> float:
    """
    finds and returns the y intercept
    """

    while x1 != 0:
        x1 = x1 - 1
        y1 = float(y1 - m)

    return y1


if __name__ == "__main__":

    x1 = float(input("Enter the x coordinate of starting point : "))
    y1 = float(input("Enter the y coordinate of starting point : "))

    x2 = float(input("Enter the x coordinate of ending point : "))
    y2 = float(input("Enter the y coordinate of ending point : "))

    m = find_slope(x1, x2, y1, y2)

    # finding the y-intercept

    b = find_y_intercept(m, x1, y1)

    # now using loop to find the coordinates
    print("X\t\tY\n\n")
    while x1 <= x2:
        print(f"{round(x1)}\t\t{round(y1)}\n")
        x1 = x1 + 1
        y1 = m * x1 + b
