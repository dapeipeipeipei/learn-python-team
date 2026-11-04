"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_if_with_multiple_elif_branches():
    """IF statement with several elif branches.

    The conditions are checked from top to bottom and only the first branch whose condition is
    true is executed, so the order of the branches matters.
    """

    def letter_grade(score):
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        return grade

    assert letter_grade(95) == 'A'
    assert letter_grade(90) == 'A'  # a boundary value belongs to the higher grade
    assert letter_grade(85) == 'B'
    assert letter_grade(72) == 'C'
    assert letter_grade(60) == 'D'
    assert letter_grade(59) == 'F'
