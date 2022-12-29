#Debugging for inheritence method
#composition:passing object as parameter to a function
class Product:
    details=""
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_save=price-deal_price
    def display_product_details(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
        print(self.ratings)
        print(self.you_save)
    def get_deal_price(self):
        return self.deal_price
class ElectronicItem(Product):
    def set_warrenty(self,warrenty):
        self.warrenty=warrenty
    def get_warrenty(self):
       return self.warrenty
class GroceryItem(Product):
    pass
class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("quantity:{}".format(quantity))
    def display_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            price=product.get_deal_price()*quantity
            total_bill+=price
        print("total bill:{}".format(total_bill))
milk=GroceryItem("milk",40,25,3.5)
tv=ElectronicItem("tv",45000,40000,3.5)
order=Order("primary delivery","hyderabad")
order.add_item(milk,2)
order.add_item(tv,1)
print("++++++")
order.display_order_details()
print("++++++")
order.display_total_bill()

##################################################################################3
#Method resolution order
class HigherParentClass:
    def print_something(self):
        print("this is from higher class")
class LowerParentClass1(HigherParentClass):
    def print_something(self):
        print("this is from lower class1")
class LowerParentClass2(HigherParentClass):
    def print_something(self):
        print("this is from lower class2")
class ChildClass(LowerParentClass1,LowerParentClass2):
    def print_something(self):
     pass
     HigherParentClass.print_something(self)#ir prints higherclass
childObj=ChildClass()
childObj.print_something()