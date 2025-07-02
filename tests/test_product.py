from unittest.mock import patch

from src.product import Product


def test_product_init(product):
    """Тест инициализации объектов класса Product"""
    assert product.name == '55" QLED 4K'
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_new_product(product_dict):
    """Тестирует создание нового товара"""
    product4 = Product.new_product(product_dict[0])

    assert product4.name == product_dict[0]["name"]
    assert product4.description == product_dict[0]["description"]
    assert product4.price == product_dict[0]["price"]
    assert product4.quantity == product_dict[0]["quantity"]


def test_new_product_update_price_and_quantity(product_dict):
    """Тестирует обновление цены и количества товара"""
    product6 = Product.new_product(product_dict[1])

    assert product6.name == product_dict[1]["name"]
    assert product6.description == product_dict[1]["description"]
    assert product6.price == product_dict[1]["price"]
    assert product6.quantity == 2


def test_product_set_lower_price(products):
    """Тестирует price-сеттер на установке меньшей цены"""
    product = products[0]
    assert product.price == 180_000  # Цена до использования сеттера

    # Установка меньшей цены
    with patch("builtins.input", return_value="y"):
        product.price = 100_000

    assert product.price == 100_000  # Цена после использования сеттера

    # Отказ при установке меньшей цены
    with patch("builtins.input", return_value="n"):
        product.price = 50_000

    assert product.price == 100_000  # Цена после использования сеттера


def test_product_set_negative_price(products):
    """Тестирует price-сеттер на установке отрицательной цены"""
    product = products[0]
    assert product.price == 100_000  # Цена до использования сеттера

    product.price = -10
    assert product.price == 100_000
