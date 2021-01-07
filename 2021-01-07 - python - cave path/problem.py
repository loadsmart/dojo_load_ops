# Parking: |


# def can_enter_the_cave(data):
#     for line in data:
#         if all(cell == 0 for cell in line):
#             return True

#     return False


def can_enter_the_cave(data, x=0, y=0):
    print(x, y)
    is_last_line = x + 1 == len(data)
    if data[x][y] != 0 and is_last_line:
        return False
    if len(data[x]) == y + 1:
        return True

    is_first_line = x == 0
    right_pos = data[x][y + 1]

    if right_pos == 0:
        return can_enter_the_cave(data, x, y + 1)

    if not is_first_line and data[x - 1][y] == 0:
        return can_enter_the_cave(data, x - 1, y)

    if not is_last_line and data[x + 1][y] == 0:
        return can_enter_the_cave(data, x + 1, y)

    if not is_last_line:
        return can_enter_the_cave(data, x + 1, 0)

    return False


def test_complex_one_not_walkable():
    data = [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
    ]
    assert can_enter_the_cave(data) == False


def test_complex_one():
    data = [
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
    ]
    assert can_enter_the_cave(data) == True


def test_can_enter_the_cave_line_with_second_lane_walkable():
    data = [[0, 1, 0, 0], [0, 0, 0, 1]]

    assert can_enter_the_cave(data) == True


def test_can_enter_the_cave_line_with_zeroes_but_not_walkable():
    data = [[0, 1, 0, 0]]

    assert can_enter_the_cave(data) == False


def test_can_enter_the_cave_only_with_zero():
    data = [[0]]

    assert can_enter_the_cave(data) == True


def test_can_enter_the_cave_only_with_one():
    data = [[1]]

    assert can_enter_the_cave(data) == False


def test_can_enter_the_cave_line_with_zeroes():
    data = [[0, 0, 0, 0]]

    assert can_enter_the_cave(data) == True


def test_can_enter_the_cave_line_with_ones():
    data = [[1, 1, 1, 1]]

    assert can_enter_the_cave(data) == False


def test_can_enter_the_cave_line_with_zeroes_and_ones():
    data = [[1, 1, 1, 1], [0, 0, 0, 0]]

    assert can_enter_the_cave(data) == True
