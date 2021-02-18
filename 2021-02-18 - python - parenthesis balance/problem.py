# Parking: |

RETURN_CORRECT = "correct"
RETURN_INCORRECT = "incorrect"


def balance_parentesis(expression):
    if not expression or not isinstance(expression, str):
        return RETURN_INCORRECT

    num_of_parentesis = 0

    for ch in expression:
        if ch == "(":
            num_of_parentesis += 1
        if ch == ")":
            if num_of_parentesis <= 0:
                return RETURN_INCORRECT
            num_of_parentesis -= 1

    return RETURN_CORRECT if not num_of_parentesis else RETURN_INCORRECT


def test_incorrect_missplaced_close_parenthesis():
    assert balance_parentesis(")(x( + x)") == RETURN_INCORRECT


def test_incorrect_expression_extra_close_parenthesis():
    assert balance_parentesis("(x)) + x)") == RETURN_INCORRECT


def test_correct_expression_one_group():
    assert balance_parentesis("(x + x)") == RETURN_CORRECT


def test_incorrect_expression_one_group():
    assert balance_parentesis("(x + x") == RETURN_INCORRECT


def test_incorrect_expression_from_test_1():
    assert balance_parentesis(")3+b*(2-c)(") == RETURN_INCORRECT


def test_incorrect_expression_from_test_1():
    assert balance_parentesis("(a+b*(2-c)-2+a)*2 ") == RETURN_CORRECT


def test_null():
    assert balance_parentesis(None) == RETURN_INCORRECT


def test_integer():
    assert balance_parentesis(2) == RETURN_INCORRECT