import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


@pytest.fixture
def sm():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0,
                      8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lg():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


def test_add(sm, lg):
    sum = 0
    with pytest.raises(TypeError):
        sum = sm + lg

    assert sum == 0
    assert sm + sm == 3360000.0
