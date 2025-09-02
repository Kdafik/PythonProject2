class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, params):
        return cls(**params)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            if input("Новая цена товара ниже старой, введите 'y' для подтверждения") == "y":
                self.__price = new_price
        else:
            self.__price = new_price
