import pytest
from app.calculator import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 3, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_succes(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
