from src.category import Category


class Tape:

    def __init__(self, category: Category):
        self.category = category.products
        self.product_count = len(self.category)

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        if self.i + 1 < self.product_count:
            self.i += 1
            return self.category[self.i]
        else:
            raise StopIteration
