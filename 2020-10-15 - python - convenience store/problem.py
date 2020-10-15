# Parking: | 

from operator import mul
values = [25, 10, 5, 1]

def is_change_enough(change, due):
    return sum(map(mul, change, values)) >= due

def test_bag_of_nickels_pennies_dimes_and_quarters():
    assert is_change_enough([1,1,1,1], 41) == True

def test_bag_of_nickels_pennies_and_dimes():
    assert is_change_enough([0,1,1,1], 17) == False

def test_bag_of_nickels_pennies_and_dimes():
    assert is_change_enough([0,1,1,1], 16) == True

def test_bag_of_nickels_and_pennies():
    assert is_change_enough([0,0,1,1], 7) == False

def test_bag_of_nickels_and_pennies():
    assert is_change_enough([0,0,1,1], 6) == True

def test_bag_of_quarter_not_enough():
    assert is_change_enough([1,0,0,0], 26) == False

def test_bag_of_quarter():
    assert is_change_enough([1,0,0,0], 25) == True

def test_poverty():
    assert is_change_enough([0,0,0,0], 10) == False

def test_pennysworth():
    assert is_change_enough([0,0,0,1], 1) == True

def test_pennywise():
    assert is_change_enough([0,0,0,1], 2) == False

def test_bag_of_pennies():
    assert is_change_enough([0,0,0,2], 2) == True

def test_bag_of_nickels():
    assert is_change_enough([0,0,1,0], 5) == True

def test_bag_of_nickels_not_enough():
    assert is_change_enough([0,0,1,0], 6) == False

def test_bag_of_dimes():
    assert is_change_enough([0,1,0,0], 10) == True

def test_bag_of_dimes_not_enough():
    assert is_change_enough([0,1,0,0], 11) == False
