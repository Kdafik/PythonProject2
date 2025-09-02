from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        product_count = 0
        for product in self.__products:
            product_count += product.quantity
        return f'{self.name}, количество продуктов: {product_count} шт.'

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> list[str]:
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return result
