# content of test_sample.py
from Group_HW1.code.main import add
from Group_HW1.code.main import subtract
from Group_HW1.code.main import multiply
from Group_HW1.code.main import divide

def test_add():
    assert add_func(3,4) == 3


def test_sub():
    assert sub_func(4,3) == 1


def test_mul():
    assert mul_func(3,4) == 12


def test_div():
    assert div_func(3,1) == 3
