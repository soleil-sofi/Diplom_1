import random
import pytest

from components.bun import Bun
from components.ingredient import Ingredient
from data_for_tests import constants as const


@pytest.fixture(scope="function")
def new_bun():
    return Bun(random.choice(const.bun_names)+" булка", random.uniform(const.min_bun_price, const.max_bun_price))


@pytest.fixture(scope="function")
def new_ingredient():
    ingredient_type = random.choice(const.ingredient_types)
    if ingredient_type == "начинка":
        ingredient_name = random.choice(const.toppings)
        ingredient_price = random.uniform(const.min_topping_price, const.max_topping_price)
    else:
        ingredient_name = random.choice(const.sauces)
        ingredient_price = random.uniform(const.min_sauces_price, const.max_sauces_price)
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)
