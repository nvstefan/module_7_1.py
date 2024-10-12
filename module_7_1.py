# Домашнее задание по теме "Режимы открытия файлов"
# Задача "Учёт товаров":


from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file1 = open(self.__file_name, 'r')
        product = file1.read()
        file1.close()
        return product

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for comp in products:
            if str(comp) in self.get_products():
                pprint(f"Продукт {str(comp)} уже есть в магазине")
            else:
                file.write(str(comp) + '\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
s1.get_products()

