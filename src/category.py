from src.product import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []

        # Добавляем начальные продукты с проверкой типа
        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def __str__(self):
        """Возвращение информации по товару в виде строки:
        Название категории, количество продуктов: _ шт."""
        total = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def add_product(self, product, update_count=True):
        """Добавление продукта с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        if product.quantity == 0:
            raise ValueError("Невозможно добавить товар с нулевым количеством.")

        else:
            self.__products.append(product)
        if update_count:
            Category.product_count += 1
        return product

    def middle_price(self):
        """Метод, который подсчитывает средний ценник всех товаров"""
        total = sum(product.price for product in self.__products)
        try:
            avg = total / len(self.__products)
        except ZeroDivisionError:
            return 0.0
        else:
            return round(avg, 2)

    @property
    def products(self):
        """Возвращает список продуктов"""
        return self.__products

    def formatted_products(self):
        """Возвращает форматированную строку с продуктами"""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )
