# content of test_sample.py

import pytest

import sys
sys.path.insert(0,'Group30_Hw1')

from code.main import add
from code.main import subtract
from code.main import multiply
from code.main import divide


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
