import pytest

from components.burger import Burger


class TestBurger:

    def test_set_buns(self, new_bun):
        burger = Burger()
        burger.set_buns(new_bun)
        assert burger.bun == new_bun

    def test_add_ingredient(self, new_ingredient):
        burger = Burger()
        burger.add_ingredient(new_ingredient)
        assert new_ingredient in burger.ingredients

    def test_remove_ingredient(self, new_ingredient):
        burger = Burger()
        burger.add_ingredient(new_ingredient)
        ingredient_index = burger.ingredients.index(new_ingredient)
        burger.remove_ingredient(ingredient_index)
        assert new_ingredient not in burger.ingredients

    def test_move_ingredient(self, new_burger, new_ingredient):
        new_burger.add_ingredient(new_ingredient)
        ingredient_index = new_burger.ingredients.index(new_ingredient)
        new_index = ingredient_index-1
        new_burger.move_ingredient(ingredient_index, new_index)
        assert new_burger.ingredients.index(new_ingredient) == new_index

    def test_get_price(self, new_burger):
        buns_price = new_burger.bun.get_price()*2
        ingredients = new_burger.ingredients
        ingredients_price = 0
        for item in ingredients:
            ingredients_price += item.get_price()
        assert int(new_burger.get_price()) == int(buns_price + ingredients_price)

    def test_get_receipt_right_bun_in_result(self, new_burger):
        assert new_burger.bun.get_name() in new_burger.get_receipt()

    @pytest.mark.parametrize("index", [0, 1])
    def test_get_receipt_right_ingredients_in_result(self, new_burger, index):
        assert new_burger.ingredients[index].get_name() in new_burger.get_receipt()

    def test_get_receipt_right_price_in_result(self, new_burger):
        assert str(new_burger.get_price()) in new_burger.get_receipt()