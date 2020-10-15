# Estacionamento |
def boomerangs(entries):
    count = 0
    for key, value in enumerate(entries[:-2]):
        if value == entries[key+1]:
            continue
        if value == entries[key+2]:
            count += 1
    return count

def test_empty_list():
    assert boomerangs([]) == 0

def test_no_boomerang_with_3_digits_list():
    assert boomerangs([1, -1, 2]) == 0

def test_boomerang_with_3_digits_list():
    assert boomerangs([1, -1, 1]) == 1

def test_boomerang_with_3_digits_list_2():
    assert boomerangs([2, 3, 2]) == 1

def test_no_boomerang_with_3_digits_identicals():
    assert boomerangs([2, 2, 2]) == 0

def test_boomerang_with_4_digits():
    assert boomerangs([2, 2, 4, 2]) == 1

def test_no_boomerang_with_4_digits():
    assert boomerangs([2, 2, 4, 4]) == 0

def test_two_boomerang_with_4_digits():
    assert boomerangs([1, 2, 1, 2]) == 2

def test_one_boomerang_with_5_digits():
    assert boomerangs([1, 1, 1, 1, 1]) == 0
