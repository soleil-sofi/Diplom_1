import random
from unittest.mock import Mock

from bun import Bun
from data_for_tests import constants as const


class TestBun:
    def test_get_name(self):
        test_name = random.choice(const.bun_names)
        bun = Bun(test_name, random.randint(0, 10))
        assert bun.get_name() == test_name

    def test_get_price(self):
        test_price = random.uniform(1, 10000)
        bun = Bun(random.choice(const.bun_names), test_price)
        assert bun.get_price() == test_price
