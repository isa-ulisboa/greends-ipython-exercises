
from teste import square
from functions import my_sqrt

def test_square():
    assert square(2)==4
    assert square(0)==0
    assert 0.9 < square(-1) < 1.1 

def test_my_sqrt():
    assert 1.4 < my_sqrt(2) < 1.42