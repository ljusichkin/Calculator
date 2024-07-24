from typing import Union


class Calculator:
    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x + y

    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x / y

    def multiply(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x * y

    def diff(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x - y

    def power(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x ** y

    def percent(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x * y / 100

    def square(self, x: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return abs(x) ** 0.5

if __name__ == '__main__':
    b = Calculator()


# a = list. #insert, remove, append, extend, clear
# b = Calculator() #add, divide, multiply, diff, power, percent, square
# pytest.ini
# pytest
# pytest -v
# pytest -s

# class def(self, )
# module
# if __name__ == '__main__'





