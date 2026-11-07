from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6