from src.utils import create_objects_from_json, read_json


def test_read_json(path_products_json, data_products_json):
    """Проверяем верно ли читается products.json"""
    assert read_json(path_products_json) == data_products_json


def test_create_objects_from_json(data_products_json):
    """Проверяем верно ли возвращаются объекты"""
    assert len(create_objects_from_json(data_products_json)) == 2
