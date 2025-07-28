import pytest


def test_smartphone_init(smartphone1):
    """Тестирует инициализацию экземпляра класса Smartphone"""
    assert smartphone1.name == "Smartphone1"
    assert smartphone1.description == "Description1"
    assert smartphone1.price == 50_000
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "Model X"
    assert smartphone1.memory == 250
    assert smartphone1.color == "Black"


def test_smartphone_add(smartphone1, smartphone2):
    """Тестирует сложение продуктов класса Smartphone"""
    assert smartphone1 + smartphone2 == 650_000


def test_smartphone_add_lawn_grass(smartphone1, lawn_grass1):
    """Тестирует сложение продуктов из разных категорий"""
    with pytest.raises(TypeError):
        smartphone1 + lawn_grass1


def test_smartphone_add_price(smartphone1):
    """Тестирует сложение продуктов класса Smartphone с ценой"""
    with pytest.raises(TypeError):
        smartphone1 + 90_000
