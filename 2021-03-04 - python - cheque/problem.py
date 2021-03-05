# Parking: |

import pytest

dict_text = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "quatorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19: "dezenove",
    20: "vinte",
    30: "trinta",
    40: "quarenta",
    50: "cinquenta",
    60: "sessenta",
    70: "setenta",
    80: "oitenta",
    90: "noventa",
    100: "cem",
}


def function_ten(value):
    remaining = value // 10  # 25 // 10 = 2
    multiple_of_ten = remaining * 10  # 2 * 10 = 20
    mod = value % 10  # 25 % 10 = 5

    return f"{dict_text[multiple_of_ten]} e {dict_text[mod]}"


def function(value):
    if value in dict_text:
        str_value = dict_text[int(value)]
    elif value < 100:
        str_value = function_ten(value)
    else:
        str_value = f"cento e {function_ten(value-100)}"

    sufix = " reais" if value > 1 else " real"
    return str_value + sufix


@pytest.mark.parametrize(
    "value, expected",
    [
        (1, "um real"),
        (2, "dois reais"),
        (3, "três reais"),
        (4, "quatro reais"),
        (5, "cinco reais"),
        (6, "seis reais"),
        (7, "sete reais"),
        (8, "oito reais"),
        (9, "nove reais"),
        (10, "dez reais"),
        (11, "onze reais"),
        (12, "doze reais"),
        (13, "treze reais"),
        (14, "quatorze reais"),
        (15, "quinze reais"),
        (16, "dezesseis reais"),
        (17, "dezessete reais"),
        (18, "dezoito reais"),
        (19, "dezenove reais"),
        (20, "vinte reais"),
        (21, "vinte e um reais"),
        (30, "trinta reais"),
        (35, "trinta e cinco reais"),
        (40, "quarenta reais"),
        (50, "cinquenta reais"),
        (60, "sessenta reais"),
        (70, "setenta reais"),
        (80, "oitenta reais"),
        (90, "noventa reais"),
        (99, "noventa e nove reais"),
        (100, "cem reais"),
        (125, "cento e vinte e cinco reais"),
        (132, "cento e trinta e dois reais"),
    ],
)
def test_function(value, expected):
    assert function(value) == expected
