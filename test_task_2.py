import pytest

from task_2 import find_it

def test_basic_move_zeros():
    assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5