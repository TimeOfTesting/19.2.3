import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.cals = Calculator

    def test_adding_success(self):
        assert self.cals.adding(self, 1, 1) == 2

    def test_zerro_division(self):
        with pytest.raises(ZeroDivisionError):
            self.cals.division(self, 1, 0)

    def test_multiply_success(self):
        assert self.cals.multiply(self, 2, 2) == 4

    def test_division_success(self):
        assert self.cals.division(self, 10, 5) == 2

    def test_subtraction_success(self):
        assert self.cals.subtraction(self, 7, 4) == 3

    def teardown(self):
        print('Выполнение метода Teardown')
