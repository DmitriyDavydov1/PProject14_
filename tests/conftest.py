import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def category_with_two_products():
    """Для тестов категории с двумя продуктами"""
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def category_with_one_product():
    """Для тестов категории с одним продуктом"""
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def category_without_products():
    """Для тестов категории без продуктов"""
    return Category(
        name="Ноутбуки", description="Переносные компьютеры, отличаются небольшими размерами и весом", products=[]
    )


@pytest.fixture
def product():
    """Для тестов инициализации объектов класса Product"""
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def path_products_json():
    """Путь до products.json"""
    return "../Pproject14_/data/products.json"


@pytest.fixture
def data_products_json():
    """Данные из products.json"""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2],
)
category2 = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [product3],
)


@pytest.fixture
def products():
    """Фикстура, использующаяся для тестирования классов Product и Category"""
    return product1, product2, product3


@pytest.fixture
def categories():
    """Фикстура, использующаяся для тестирования класса Category"""
    return category1, category2


@pytest.fixture
def product_dict():
    """Фикстура, использующаяся для тестирования классов Product и Category"""
    return (
        {"name": "Phone", "description": "Some description", "price": 10000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 20000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 5000, "quantity": 1},
    )


@pytest.fixture
def smartphone1():
    """Фикстура для тестирования класса Smartphone"""
    return Smartphone("Smartphone1", "Description1", 50_000.0, 5, 98.2, "Model X", 250, "Black")


@pytest.fixture
def smartphone2():
    """Фикстура для тестирования класса Smartphone"""
    return Smartphone("Smartphone2", "Description2", 40_000.0, 10, 78.2, "Model Y", 150, "White")


@pytest.fixture
def lawn_grass1():
    """Фикстура для тестирования класса LawnGrass"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass2():
    """Фикстура для тестирования класса LawnGrass"""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
