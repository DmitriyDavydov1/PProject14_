class PrintMixin:
    """
    Класс-миксин,
    который при создании объекта печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self):
        """Инициализация и вывод представления объекта."""
        print(repr(self))

    def __repr__(self):
        """Dunder-метод для возврата строкового представление объекта."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
