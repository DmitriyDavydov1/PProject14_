from typing import List


class Product:
    # Атрибут на уровне класса для хранения экземпляров класса в виде списка
    all_products: List["Product"] = list()

    name: str  # название
    description: str  # описание
    price: int  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        """Инициализация экземпляра класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products.append(self)

    @classmethod
    def new_product(cls, product_dict):
        """Класс-метод для создания нового продукта или обновления существующего."""
        name = product_dict.get("name", "")
        description = product_dict.get("description", "")
        price = product_dict.get("price", 0.0)
        quantity = product_dict.get("quantity", 0)

        # Проверка наличия такого же товара схожего по имени
        for product in Product.all_products:
            if name == product.name:
                # Обновление количества товара
                product.quantity += quantity
                # Обновление цены, если новая цена выше
                if price > product.price:
                    product.price = price
                return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, amount):
        """Сеттер для установки цены."""
        if amount <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif amount < self.__price:
            difference = self.__price - amount
            confirmation = input(f"Вы уверены, что хотите снизить цену на {difference} руб? (y/n): ").lower()
            if confirmation == "y":
                self.__price = amount
            else:
                print("Цена осталась прежней")
        else:
            self.__price = amount
