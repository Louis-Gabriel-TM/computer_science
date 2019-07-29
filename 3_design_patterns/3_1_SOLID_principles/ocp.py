# OCP = Open-Closed Principle (2nd SOLID principle):
# "A class / module / function / ... should be open for extension, but closed for modification."

from enum import Enum


class Color(Enum):

    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):

    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:

    def __init__(self, name, color, size):
        self.size = size
        self.color = color
        self.name = name


# A bad naive design:
class ProductFilter:
    # The methods below filter products for some requirement or combinaison of requirements.
    # They should form a too long piece of code, hard to maintain.

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


# The Enterprise Pattern Specification can solve this problem:
class Specification:  # abstract base class

    def is_satified(self, item):
        pass

    def __and__(self, other):  # syntax sugar
        return AndSpecification(self, other)


class Filter:  # abstract base class

    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satified(self, item):
        return item.color == self.color


class SizeSpecification(Specification):

    def __init__(self, size):
        self.size = size

    def is_satified(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satified(item):
                yield item


# Use a combinator for multiple requirements:
class AndSpecification(Specification):

    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satified(self, item):
        return self.spec1.is_satified(item) and self.spec2.is_satified(item)


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Filtering with a naive filter
    pf = ProductFilter()

    print("Green prodcts with naive filter:")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f"  - {p.name} is green.")

    # Filtering with a better filter
    bf = BetterFilter()

    print("Grren products with a better designed filter:")
    green_spec = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green_spec):
        print(f"  - {p.name} is green.")

    print("Large products with a better designed filter:")
    large_spec = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large_spec):
        print(f"  - {p.name} is large.")

    print("Large blue products with a combinator:")
    large_blue_spec = large_spec and ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue_spec):
        print(f"  - {p.name} is large and blue.")
