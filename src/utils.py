import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    # Получаем абсолютный путь относительно текущего файла
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, '..', path)

    # Нормализуем путь (убираем ../ и т.д.)
    full_path = os.path.normpath(full_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Файл не найден: {full_path}")

    with open(full_path, "r", encoding="UTF-8") as file:
        return json.load(file)

def create_objects_from_json(data):
    categories = []
    for category_data in data:
        # Создаем список продуктов
        products = []
        for product_data in category_data["products"]:
            # Создаем объект Product из словаря
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"]
            )
            products.append(product)

        # Создаем категорию с продуктами
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)
    return categories
