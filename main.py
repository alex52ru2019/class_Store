class Store:
    def __init__(self, name, addr):
        self.name = name # название магазина.
        self.address = addr # адрес магазина.
        self.item = {} # словарь, где ключ - название товара, а значение - его цена.
                       # например, {'apples': 0.5, 'bananas': 0.75}.

    def product_add(self, product, price): # метод для добавления товара в ассортимент
        self.item[product] = price

    def product_del(self, product): # метод для удаления товара из ассортимента
        self.item.pop(product)

    def get_price(self, product): # метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None
        print(f"цена {product} = {self.item.get(product)}")

    def set_price(self, product, price): # метод для обновления цены товара
        self.item.update({product: price})
        print(f"новая цена {product} = {self.item.get(product)}")

    def all_info(self):  # метод для вывода всей инфорации
        print(f"Магазин {self.name}\n"
              f"адрес магазина {self.address}\n"
              f"Ассортимент:\n {self.item.items()}\n")

#создал магазин
mag_1 = Store("Ромашка", "Россия, Москва")
#добавляю товары
mag_1.product_add("Пиво", 200)
mag_1.product_add("Вобла", 100)
mag_1.product_add("Мясо", 300)
mag_1.product_add("Шоколад", 50)
mag_1.product_add("Кофе", 300)
mag_1.product_add("Чай", 57.50)

mag_1.all_info() # информация по магазину

mag_1.product_del("Мясо") # удалил товар
mag_1.product_del("Шоколад")  # удалил товар

mag_1.all_info() # информация по магазину

mag_1.get_price("Кофе") # узнать цену

mag_1.set_price("Кофе", 299.99)  # установить цену

mag_1.all_info() # информация по магазину
