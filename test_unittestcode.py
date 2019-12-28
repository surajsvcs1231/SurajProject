import unittest
import unittestcode
class TestUnittestcode(unittest.TestCase):
    def test_add(self):
        #result=unittestcode.add(5,14)
        #self.assertEquals(result,19)
        self.assertEqual(unittestcode.add(5,14),19)
        self.assertEqual(unittestcode.add(-1,1),0)
        self.assertEqual(unittestcode.add(-1,-1),-2)
    def test_subtract(self):
        self.assertEqual(unittestcode.subtract(14,9),5)
    def test_multiply(self):
        self.assertEqual(unittestcode.multiply(10,9),90)
    def test_division(self):
        self.assertEqual(unittestcode.divide(14,2),7)
        #self.assertEquals(unittestcode.divide(14,2),7.5)
        #self.assertEquals(unittestcode.divide(14, 0), 7.5)
        #self.assertRaises(ValueError,unittestcode.divide,10,2)


if __name__=='__main__':
    unittest.main()

