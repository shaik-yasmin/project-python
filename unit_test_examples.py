'''import unittest
class upper_class(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    def test_lower(self):
        self.assertEqual('go'.lower(),'go')
    def test_islower(self):
        self.assertTrue('hi'.islower())
    def test_isupper(self):
        self.assertFalse('hlo'.isupper())
    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])
        self.assertRaises(TypeError)
        s.split(" ")
if __name__=="main":
    unittest.main()'''

import unittest
class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget=Widget('the Widget')
        self.assertEqual(widget.size(),(50,50))
class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")


