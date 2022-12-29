from using_property import Student
import unittest
st = Student("hcl", "tech",10,2022,12)
class test_Student(unittest.TestCase):
   def setUp(self):
       print("\nsetup")
   def tearDown(self):
       print("\nteardown")
   def test_email(self):
       self.assertEqual(st.email,"hcl.tech@gmail.com")
   def test_fullname(self):
       self.assertEqual(st.fullname,"hcl.tech")
   def test_apply_bonus(self):
       st.apply_bonus()
       self.assertEqual(st.marks,20)
   def test_dummy(self):
       st.dummy()
       self.assertEqual(st.year,2023)
   def test_class_name(self):
       st.dummy1()
       self.assertEqual(st.class_name,12)
   def test_something(self):
       st.something("vij")
       self.assertEqual(st.somevalue,"hcl.tech@gmail.comhcl.techvij")
   def test_something1(self):
       #self.assertEqual(st.something1,"hcl.tech@gmail.comhcl.tech")
       st.something1()
if __name__=="__main__":
    unittest.main()

