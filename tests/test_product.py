def test_product_init(product):
    """Тест инициализации объектов класса Product"""
    assert product.name == '55" QLED 4K'
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7
