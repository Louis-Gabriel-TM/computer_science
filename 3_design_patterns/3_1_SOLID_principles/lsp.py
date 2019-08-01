"""
LSP = (Barbara) Liskov Substitution Principle (3rd SOLID principle):

    "Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program."

"""


class Rectangle:

    # A class with protected attributes
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    # The getters and setters of the attributes
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self):
        return f"Width: {self.width} | Height: {self.height}"


class Square(Rectangle):

    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # This setters will break the LSP
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rect):
    # Beacause LSP is broken, this function will work with a Rectangle but not with a Square
    w = rect.width
    rect.height = 10
    expected = w * 10
    print(f"Expected an area of {expected}, got {rect.area}")


if __name__ == "__main__":
    # First, everything goes fine
    rect = Rectangle(2, 3)
    use_it(rect)

    # But the LSP is broken with the child class, causing side effects
    sq = Square(5)
    use_it(sq)

    # Solutions to this problem:
    #   - is the Square class really useful ?
    #   - using a Factory pattern
    #   - ...
