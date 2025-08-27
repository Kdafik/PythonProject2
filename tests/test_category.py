import pytest

from src.category import Category


@pytest.fixture
def category_phones():
    Category("Another", "another", [1, 1, 1])
    return Category("Phones", "phones", [1, 1, 1])


def test_init(category_phones):
    assert category_phones.name == "Phones"
    assert category_phones.description == "phones"
    assert category_phones.products == [1, 1, 1]
    assert Category.category_count == 2
    assert Category.product_count == 6
