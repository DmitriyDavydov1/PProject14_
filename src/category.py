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
            self.add_product(product, update_count=False)

        Category.category_count += 1

    def add_product(self, product, update_count=True):
        """Добавление продукта с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        if update_count:
            Category.product_count += 1
        return product

    @property
    def products(self):
        """Форматированный вывод продуктов"""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products)
