import pytest

from src.product import Product


@pytest.fixture
def product_iphone():
    return Product("Iphone 11", "Iphone 11", 1000.0, 5)


def test_init(product_iphone):
    assert product_iphone.name == "Iphone 11"
    assert product_iphone.description == "Iphone 11"
    assert product_iphone.price == 1000.0
    assert product_iphone.quantity == 5
