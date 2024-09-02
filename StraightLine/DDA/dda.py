"""
Program to find the coordinates of line to draw using 
DDA alogrithm
"""

if __name__ == "__main__":

    # takking the inputs
    x1 = float(input("Enter the x-coordinate of starting point :"))
    y1 = float(input("Enter the y-coordinate of starting point :"))

    x2 = float(input("Enter the x-coordinate of ending point :"))
    y2 = float(input("Enter the y-coordinate of ending point :"))

    # findin the total increase in x and y

    dx = x2 - x1
    dy = y2 - y1

    steplength = abs(dx) if abs(dx) >= abs(dy) else abs(dy)

    x_inc = dx / steplength
    y_inc = dy / steplength

    # finding the coordinates

    print("X\t\tY\n\n")
    i = 0

    while i <= steplength:
        print(f"{x1}\t\t{y1}")
        x1 = x1 + x_inc
        y1 = y1 + y_inc

        i = i + 1
