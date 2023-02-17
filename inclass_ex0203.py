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
    c = y1 - (m*x1)
    return c


def find_y(x, m, c):
    y = m*x + c
    return y


def find_coordinate(coord1, coord2, x):
    m = find_gradient(coord1, coord2)
    c = find_y_intercept(m, coord1)
    y = find_y(x, m, c)
    print(y)
    return y


if __name__ == "__main__":
    find_coordinate((1, 1), (2, 2), 3)
