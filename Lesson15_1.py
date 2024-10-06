class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # method to calculate the area
    def get_square(self):
        return self.width * self.height

    # comparing two rectangles by area
    def __eq__(self, other):
        return self.get_square() == other.get_square()

    # a method for adding two rectangles
    def __add__(self, other):
        total_area = self.get_square() + other.get_square()
        new_width = self.width
        # other side is calculated as area / width
        new_height = total_area // new_width
        return Rectangle(new_width, new_height)

    # multiplying a rectangle by the n
    def __mul__(self, n):
        new_area = self.get_square() * n
        # select the width and calculate the height
        new_width = self.width
        new_height = new_area // new_width
        return Rectangle(new_width, new_height)

    # lil prettier here
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"

# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(r1)  # Rectangle(width=2, height=4, area=8)
print(r2)  # Rectangle(width=3, height=6, area=18)
print(r3)  # Rectangle(width=?, height=?, area=26)
print(r4)  # Rectangle(width=?, height=?, area=32)
