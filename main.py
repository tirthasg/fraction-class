class Fraction:
  _counter = 0

  def __init__(self, numerator, denominator):
    gcd = self._gcd(numerator, denominator)
    
    self._numerator = numerator // gcd
    self._denominator = denominator // gcd

    Fraction._counter += 1

  @property
  def numerator(self):
    return self._numerator

  @numerator.setter
  def numerator(self, value):
    self._numerator = value

  @property
  def denominator(self):
    return self._denominator

  @denominator.setter
  def denominator(self, value):
    self._denominator = value

  def __str__(self):
    return f'{self._numerator} / {self._denominator}'

  def __repr__(self):
    return f'ID={id(self)}, Numerator={self._numerator}, Denominator={self._denominator}'

  def _gcd(self, a, b):
    if a == 0:
      return b

    if b == 0:
      return a
    
    while b % a != 0:
      rem = b % a
      b = a
      a = rem

    return a

  def __add__(self, other):
    res_numerator = self._numerator * other._denominator + self._denominator * other._numerator
    res_denominator = self._denominator * other._denominator
    
    gcd = self._gcd(res_numerator, res_denominator)
    res_numerator //= gcd
    res_denominator //= gcd

    return Fraction(res_numerator, res_denominator)

  @classmethod
  def get_counter(cls):
    return cls._counter

  @staticmethod
  def is_valid_denominator(value):
    return value != 0
    
    
    
f1 = Fraction(6, 8)
print(f1)
print(repr(f1))
print(Fraction.get_counter())

f2 = Fraction(2, 8)
print(f2)
print(repr(f2))
print(Fraction.get_counter())

f3 = f1 + f2
print(f3)
print(repr(f3))
print(Fraction.get_counter())

print(Fraction.is_valid_denominator(0))
print(Fraction.is_valid_denominator(10))