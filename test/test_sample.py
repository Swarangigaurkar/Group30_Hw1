# content of test_sample.py

import sys
sys.path.insert(0,'Swarangigaurkar/Group30_Hw1/code')

from main import add
from main import subtract
from main import multiply
from main import divide


#test add function
def test_add():
    assert add(3,4) == 7

#test subtract function
def test_sub():
    assert subtract(4,3) == 1

#test multiply function
def test_mul():
    assert multiply(3,4) == 12

#test divide function
def test_div():
    assert divide(3,1) == 3
    

test_add()
test_sub()
test_mul()
test_div()
