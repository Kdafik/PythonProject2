import pytest

from src.product import Product


@pytest.fixture
def product_iphone():
    return Product("Iphone 11", "Iphone 11", 1000.0, 5)


@pytest.fixture
def dict_product():
    return {"name": "Iphone 11", "description": "Iphone 11", "price": 1000.0, "quantity": 5}


def test_init(product_iphone):
    assert product_iphone.name == "Iphone 11"
    assert product_iphone.description == "Iphone 11"
    assert product_iphone.price == 1000.0
    assert product_iphone.quantity == 5


def test_new_product(product_iphone, dict_product):
    new_product = Product.new_product(dict_product)
    assert new_product.name == "Iphone 11"
    assert new_product.description == "Iphone 11"
    assert new_product.price == 1000.0
    assert new_product.quantity == 5


def test_price(product_iphone, monkeypatch):
    product_iphone.price = -100
    assert product_iphone.price == 1000.0
    product_iphone.price = 0
    assert product_iphone.price == 1000.0

    monkeypatch.setattr('builtins.input', lambda _: "y")
    product_iphone.price = 800
    assert product_iphone.price == 800.0
    product_iphone.price = 1100
    assert product_iphone.price == 1100.0
