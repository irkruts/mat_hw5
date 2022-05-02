class Calculator:
    def add(self, a, b):
        pass


class IntegerCalculator(Calculator):
    def __init__(self):
        self.sum = 0

    def add(self, x, y):
        self.sum += (x + y)

    def __str__(self):
        return f'{int(self.sum)}'


class FloatCalculator(Calculator):
    def __init__(self):
        self.sum = 0

    def add(self, x, y):
        self.sum += (x + y)

    def __str__(self):
        return f'{float(self.sum)}'


def make_add(fnc, num_1, num_2_2):
    if isinstance(fnc, IntegerCalculator):
        fnc.add(num_1, num_2_2)
        return fnc
    if isinstance(fnc, FloatCalculator):
        fnc.add(num_1, num_2_2)
        return fnc


int_calc = IntegerCalculator()
result = make_add(int_calc, 1.0, 2.0)
print(result)
float_calc = FloatCalculator()
result = make_add(float_calc, 1, 2)
print(result)
