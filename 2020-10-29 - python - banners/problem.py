# Parking: |


def banner_area(buildings):
    results = []
    # [(ind, b), ]
    augment = list(enumerate(buildings))
    augment.sort(reverse=True)
    support = [(0, 0), ()]

    for i in range(len(buildings)):
        left = buildings[:i]
        right = buildings[i:]
        area_left = max(left) * len(left) if left else 0
        area_right = max(right) * len(right) if right else 0
        results.append(area_left + area_right)
    return min(results)


def test_banner_quebrar():
    assert banner_area([1 for i in range(10000)]) == 10000


def test_banner_7777777877777771():
    assert banner_area([7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 1]) == 120


def test_banner_777177():
    assert banner_area([7, 7, 7, 1, 7, 7]) == 42


def test_banner_6761():
    assert banner_area([6, 7, 6, 1]) == 22


def test_banner_area_for_another_three_buildings_11():
    assert banner_area([5, 2, 3]) == 11


def test_banner_area_for_another_three_buildings_11():
    assert banner_area([5, 2, 3]) == 11


def test_banner_area_for_another_three_buildings():
    assert banner_area([5, 2, 1]) == 9


def test_banner_area_for_three_buildings():
    assert banner_area([1, 2, 2]) == 5


def test_banner_area_for_three_buildings_size_one():
    assert banner_area([1, 2, 1]) == 5


def test_banner_area_for_one_building_size_one():
    assert banner_area([1]) == 1


def test_banner_area_for_one_building_size_two():
    assert banner_area([2]) == 2


def test_banner_area_for_two_buildings_size_one():
    assert banner_area([1, 1]) == 2


def test_banner_area_for_two_buildings_size_one():
    assert banner_area([1, 2]) == 3
