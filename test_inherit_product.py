from debuginherit import Product
import unittest
obj=Product("milk",30,25,5)
class test_Product:
    @classmethod
    def setUpclass(self):
        print("\nsetup")
    @classmethod
    def tearDownclass(self):
        print("\nteardown")
    def test_display_product_details(self):
        obj.display_product_details()
        self.assertEqual(obj.details,"milk",30,25,5)
    def test_get_deal_price(self):
        obj.get_deal_price()
        self.assertEqual(obj.get_deal_price,25)
class test_ElectronicItem(Product):
    @classmethod
    def setupclass(self):
        print("\nsetup")
    @classmethod
    def teardownclass(self):
        print("\nteardown")
    def test_get_warrenty(self):
        obj.get_warrenty(2024)
        self.assertEqual(obj.get_warrenty,2024)

if __name__=="main":
    unittest=main()

