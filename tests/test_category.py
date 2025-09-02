import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def p():
    return Product("Iphone 11", "Iphone 11", 1000.0, 5)


@pytest.fixture
def sm():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0,
                      8, 98.2, "15", 512, "Gray space")


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


def test_add_product(category_phones, p, sm):
    category_phones.add_product(p)
    assert len(category_phones.products) == 4
    with pytest.raises(TypeError):
        category_phones.add_product("not product")

    assert len(category_phones.products) == 4
    category_phones.add_product(sm)
    assert len(category_phones.products) == 5


def test_products(category_phones, products):
    assert category_phones.products == products


def test_str(category_phones):
    assert str(category_phones) == "Phones, количество продуктов: 15 шт."
