import pytest

from src.category import Category
from src.product import Product
from src.tape import Tape


@pytest.fixture
def p():
    return Product("Iphone 11", "Iphone 11", 1000.0, 5)


@pytest.fixture
def category_phones(p):
    return Category("Phones", "phones", [p, p, p])


def test_init(category_phones):
    i = 0
    for product in Tape(category_phones):
        i += 1
    assert i == 3
