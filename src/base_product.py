from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для представления продукта."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Абстрактный класс-метод для создания нового продукта или обновления существующего."""
        pass
