from typing import Union


class Calculator:
    def add(self, a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
        pass


class IntegerCalculator(Calculator):
    def add(self, x: Union[float, int], y: Union[float, int]) -> int:
        return int(x + y)


class FloatCalculator(Calculator):
    def add(self, x: Union[float, int], y: Union[float, int]) -> float:
        return float(x + y)


def make_add(fnc, num_1: Union[float, int], num_2_2: Union[float, int]) -> Union[float, int]:
    return fnc.add(num_1, num_2_2)


int_calc = IntegerCalculator()
result = make_add(int_calc, 1.0, 2.0)
print(result)
float_calc = FloatCalculator()
result = make_add(float_calc, 1, 2)
print(result)
