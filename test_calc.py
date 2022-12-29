import calc
import unittest
class tetsCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,15),25)
    def test_sub(self):
        self.assertEqual(calc.sub(15,10),5)
    def test_mul(self):
        self.assertEqual(calc.mul(5,10),50)
    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
if __name__=="__main__":
    unittest.main()


