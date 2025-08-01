import pytest


def test_lawn_grass_init(lawn_grass1):
    """Тестирует инициализацию экземпляра класса LawnGrass"""
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass1, lawn_grass2):
    """Тестирует сложение продуктов класса LawnGrass"""
    assert lawn_grass1 + lawn_grass2 == 16_750


def test_smartphone_add_smartphone(lawn_grass2, smartphone2):
    """Тестирует сложение продуктов из разных категорий"""
    with pytest.raises(TypeError):
        lawn_grass2 + smartphone2


def test_smartphone_add_price(lawn_grass1):
    """Тестирует сложение продуктов класса LawnGrass с ценой"""
    with pytest.raises(TypeError):
        lawn_grass1 + 1000
