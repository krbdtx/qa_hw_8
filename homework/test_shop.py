"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import *


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1100)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500) is True
        assert product.check_quantity(1500) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(600)
        assert product.check_quantity(500)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1500)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, 6)
        assert cart.products[product] == 6

    def test_remove_product(self, product, cart):
        cart.add_product(product, 6)
        cart.remove_product(product, 6)
        assert product not in cart.products.keys()

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 100)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 3)
        assert cart.get_total_price() == 300

    def test_cart_buy(self, product, cart):
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity == 1098

        cart.add_product(product, 1200)
        with pytest.raises(ValueError):
            cart.buy()

        product.quantity = 0
        cart.add_product(product, 2)
        with pytest.raises(ValueError):
            cart.buy()
