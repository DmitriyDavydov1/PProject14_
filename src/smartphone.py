from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфона"""

    name: str
    description: str
    price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Конструктор для инициализации экземпляра класса Smartphone."""
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        """Метод для сложения товаров и получения полной стоимости всех товаров на складе"""
        if type(other) is Smartphone:
            return round(self.price * self.quantity + other.price * other.quantity)
        raise TypeError()
    