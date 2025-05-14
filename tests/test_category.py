def test_category_init(category_without_products):
    """Тест инициализации объектов класса Category"""
    assert category_without_products.name == "Ноутбуки"
    assert category_without_products.description == "Переносные компьютеры, отличаются небольшими размерами и весом"
    assert len(category_without_products.products) == 0


def test_product_count(category_with_two_products):
    assert category_with_two_products.product_count == 2


def test_category_count(category_with_one_product):
    assert category_with_one_product.category_count == 3
