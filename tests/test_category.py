import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def p():
    return Product("Iphone 11", "Iphone 11", 1000.0, 5)


@pytest.fixture
def category_phones(p):
    Category("Another", "another", [p, p, p])
    return Category("Phones", "phones", [p, p, p])


@pytest.fixture
def products():
    return ['Iphone 11, 1000.0 руб. Остаток: 5 шт.',
            'Iphone 11, 1000.0 руб. Остаток: 5 шт.',
            'Iphone 11, 1000.0 руб. Остаток: 5 шт.']


def test_init(category_phones, p, products):
    assert category_phones.name == "Phones"
    assert category_phones.description == "phones"
    assert category_phones.products == products
    assert Category.category_count == 2
    assert Category.product_count == 6


def test_add_product(category_phones, p):
    category_phones.add_product(p)
    assert len(category_phones.products) == 4


def test_products(category_phones, products):
    assert category_phones.products == products
