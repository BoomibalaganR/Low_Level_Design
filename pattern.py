def square_star(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


def hallow_square_star(n):
    for i in range(n):
        for j in range(n):
            if i in (0, n - 1) or j in (0, n - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()


def rhombus_star(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(n):
            print("*", end="")
        print()


def mirrored_rhombus_star(n):
    for i in range(n):
        for j in range(0, n - i):
            print(" ", end="")
        for k in range(n):
            print("*", end="")
        print()


def left_slide_triangle(n):
    for i in range(n):
        for j in range(0, i + 1):
            print("*", end="")
        print()


def hallow_left_slide_triangle(n):
    for i in range(n):
        for j in range(0, i + 1):
            if i == j or i == n - 1 or j == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def mirror_left_slide_triangle(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(n - i):
            print("*", end="")
        print()


def hallow_mirror_left_slide_triangle(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(n - i):
            if k == 0 or i == 0 or i + k == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def right_slide_triangle(n):
    for i in range(n):
        for j in range(0, n - i - 1):
            print("-", end="")
        for k in range(0, i + 1):
            print("*", end="")
        print()


def hallow_right_slide_triangle(n):
    for i in range(n):
        for j in range(0, n - i - 1):
            print(" ", end="")
        for k in range(0, i + 1):
            if k == 0 or i == k or k == n - 1 or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def mirror_right_slide_triangle(n):
    for i in range(n):
        for k in range(n - i):
            print("*", end="")
        print()


def pyramid_star(n):
    for i in range(n):
        for _ in range(n - i):
            print(" ", end="")
        for _ in range(i - 1):
            print("*", end="")

        for _ in range(i):
            print("*", end="")
        print()


def invert_pyramid_star(n):
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        for _ in range(n - i - 1):
            print("*", end="")
        for _ in range(n - i):
            print("*", end="")
        print()


def hallow_pyramid_star(n):
    for i in range(n):
        for j in range(0, n - i - 1):
            print(" ", end="")
        for k in range(0, i):
            if k == 0 or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(0, i + 1):
            if i == j or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def invert_hallow_pyramid_star(n):
    pass


if __name__ == "__main__":
    hallow_pyramid_star(15)
