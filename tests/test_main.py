import pytest

from contextlib import nullcontext as does_not_raise
from src.main import Calculator


class TestCalculator:
    @pytest.mark.parametrize("x, y, res, expectation",
                             [
                                 (1.0, 2, 3.0, does_not_raise()),
                                 (0, 0, 0, does_not_raise()),
                                 (-1, 1, 0, does_not_raise()),
                                 ('a', -1, 2, pytest.raises(TypeError, match='^Both arguments should be numeric$')),
                                 (1, '$', 3, pytest.raises(TypeError, match='^Both arguments should be numeric$'))
                             ])
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res

    @pytest.mark.parametrize("x, y, res, expectation",
                             [
                                 (1, 2, 0.5, does_not_raise()),
                                 (6, 3, 2, does_not_raise()),
                                 (10, 5.0, 2.0, does_not_raise()),
                                 (3, 0, 0, pytest.raises(ZeroDivisionError, match='^Cannot divide by zero$')),
                                 (3, 'a', 1.5, pytest.raises(TypeError, match='^Both arguments should be numeric$')),
                                 ('1', 3, 1.5, pytest.raises(TypeError, match='^Both arguments should be numeric$')),
                                 (0.2, 0.2, 1, does_not_raise())
                             ])
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize("x, y, res, expectation",
                             [
                                 (5, 5, 25, does_not_raise()),
                                 (2, 3.0, 6, does_not_raise()),
                                 (1, 0, 0, does_not_raise()),
                                 (-5, -2, 10, does_not_raise()),
                                 ('1', 5, 5, pytest.raises(TypeError, match='^Both arguments should be numeric$')),
                                 (5, 'b', 5, pytest.raises(TypeError, match='^Both arguments should be numeric$'))
                             ])
    def test_multiply(self, x, y, res, expectation):
        with expectation:
            assert Calculator().multiply(x, y) == res

    @pytest.mark.parametrize("x, y, res, expectation",
                             [
                                 (1, 0, 1, does_not_raise()),
                                 (10, 5, 5, does_not_raise()),
                                 (5, 10, -5, does_not_raise()),
                                 (-3, -2, -1, does_not_raise()),
                                 ('a', 5, 3, pytest.raises(TypeError, match='^Both arguments should be numeric$')),
                                 (-5, '&', 3, pytest.raises(TypeError, match='^Both arguments should be numeric$'))
                             ])
    def test_diff(self, x, y, res, expectation):
        with expectation:
            assert Calculator().diff(x, y) == res

    @pytest.mark.parametrize('x, y, res, expectation',
                             [
                                 (2, 2, 4, does_not_raise()),
                                 (3, 3, 27, does_not_raise()),
                                 (-5, 2, 25, does_not_raise()),
                                 (1, 0, 1, does_not_raise()),
                                 (' ', 6, 3, pytest.raises(TypeError, match='^Both arguments should be numeric$')),
                                 (5, '*', 3, pytest.raises(TypeError, match='^Both arguments should be numeric$'))
                             ])
    def test_power(self, x, y, res, expectation):
        with expectation:
            assert Calculator().power(x, y) == res

    @pytest.mark.parametrize('x, y, res, expectation',
                             [
                                 (10, 5, 0.5, does_not_raise()),
                                 (100, 30, 30, does_not_raise()),
                                 (50, 50, 25, does_not_raise()),
                                 (10, 0, 0, does_not_raise()),
                                 (5, -2, -0.1, does_not_raise()),
                                 ('#', 5, 100, pytest.raises(TypeError, match='^Both arguments should be numeric$')),
                                 (3, 'a', 5, pytest.raises(TypeError, match='^Both arguments should be numeric$'))
                             ])
    def test_percent(self, x, y, res, expectation):
        with expectation:
            assert Calculator().percent(x, y) == res

    @pytest.mark.parametrize('x, res, expectation',
                             [
                                 (25, 5, does_not_raise()),
                                 (10, 3.1622776601683795, does_not_raise()),
                                 (-49, 7, does_not_raise()),
                                 (5.5, 2.345207879911715, does_not_raise()),
                                 (0, 0, does_not_raise()),
                                 ('a', 10, pytest.raises(TypeError, match='^Both arguments should be numeric$'))
                             ])
    def test_square(self, x, res, expectation):
        with expectation:
            assert Calculator().square(x) == res

