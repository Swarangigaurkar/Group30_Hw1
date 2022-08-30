# content of test_sample.py
from Group_HW1.code.main import add
from Group_HW1.code.main import subtract
from Group_HW1.code.main import multiply
from Group_HW1.code.main import divide


#test add method
def test_add():
    assert add(3,4) == 7

#test subtract method
def test_sub():
    assert subtract(4,3) == 1

#test multiply method
def test_mul():
    assert multiply(3,4) == 12

#test divide method
def test_div():
    assert divide(3,1) == 3
