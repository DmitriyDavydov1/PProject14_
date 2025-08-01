import pytest

from src.category import Category
from src.product import Product


def test_category_init(category_without_products):
    """Тест инициализации объектов класса Category"""
    assert category_without_products.name == "Ноутбуки"
    assert category_without_products.description == "Переносные компьютеры, отличаются небольшими размерами и весом"
    assert len(category_without_products.products) == 0


def test_product_count(category_with_two_products):
    assert category_with_two_products.product_count == 5


def test_category_count(category_with_one_product):
    assert category_with_one_product.category_count == 5


def test_add_product(categories, products):
    """Тестирует метод add_product"""
    categories[0].add_product(products[2])
    assert Category.product_count == 7


def test_category_str(categories):
    """Тестирует отображение информации о категории в виде строки"""
    category = categories[0]
    assert str(category) == "Смартфоны, количество продуктов: 20 шт."

def test_category_add_product_zero_error(capsys, categories):
    """Тестирует метод add_product с нулевым количеством товара"""
    with pytest.raises(ValueError):
        Product("Тест", "Количество: 0", 10, 0)


def test_avg_price(categories):
    """Тестирует подсчет среднего ценника всех товаров"""
    assert categories[0].middle_price() == 171_000.0


def test_middle_price_empty():
    """Тестирует подсчет среднего ценника в пустом списке товаров"""
    category = Category("Category", "Description", [])
    assert category.middle_price() == 0.0