
from wordle_jy3482 import validate_guess, check_guess

def test_validate_guess():
    assert validate_guess("apple") is True
    assert validate_guess("Apple") is False
    assert validate_guess("apps")  is False
    assert validate_guess("app1e") is False

def test_check_guess_basic():
    # all green
    assert check_guess("crane","crane") == [
        ('c','green'),('r','green'),('a','green'),('n','green'),('e','green')
    ]
    # classic mixed example
    assert check_guess("crane","react") == [
        ('r','yellow'),('e','yellow'),('a','green'),('c','yellow'),('t','gray')
    ]
