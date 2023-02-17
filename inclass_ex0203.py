def find_gradient(coord1, coord2):
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]
    m = (y2 - y1)/(x2-x1)
    return m


def find_y_intercept(m, coord1):
    x1 = coord1[0]
    y1 = coord1[1]
    c = y1 - (m * x1)
    return c


def find_y(x, m, c):
    y = m*x + c
    return y


def find_coordinate(coord1, coord2, x):
    m = find_gradient(coord1, coord2)
    c = find_y_intercept(m, coord1)
    y = find_y(x, m, c)
    return y


# Additional Work
def check_line_validity(coord1, coord2, coord3):
    m = find_gradient(coord1, coord2)
    c = find_y_intercept(m, coord1)
    x3 = coord3[0]
    y3 = coord3[1]
    if m*x3 + c == y3:
        return True
    else:
        return False


if __name__ == "__main__":
    find_coordinate((1, 1), (2, 2), 3)
    check_line_validity((1, 1), (2, 2), (2, 1))
