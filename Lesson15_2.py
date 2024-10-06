class Fraction:

    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b

    # calculating the greatest common divisor
    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # reducing a fraction to its lowest
    def _reduce(self):
        gcd = self._gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    # multiplying fractions
    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    # adding fractions
    def __add__(self, other):
        common_denominator = self.b * other.b
        new_a = self.a * other.b + other.a * self.b
        return Fraction(new_a, common_denominator)

    # subtracting fractions
    def __sub__(self, other):
        common_denominator = self.b * other.b
        new_a = self.a * other.b - other.a * self.b
        return Fraction(new_a, common_denominator)

    # comparison for equality
    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    # checks for >
    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    # checks for <
    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    # displaying a fraction as a str
    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')