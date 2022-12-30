import pytest

from task_6 import Person

def test_person():
    joe = Person('Joe', 'Smith', 30)
    assert(joe.full_name, 'Joe Smith')
    assert(joe.age, 30)