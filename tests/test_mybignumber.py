import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mybignumber import MyBigNumber


class TestMyBigNumber(unittest.TestCase):
    
    def setUp(self):
        self.bn = MyBigNumber()
    
    def test_basic_addition(self):
        result = self.bn.sum("1234", "897")
        self.assertEqual(result, "2131")
    
    def test_addition_with_carry(self):
        result = self.bn.sum("999", "1")
        self.assertEqual(result, "1000")
    
    def test_large_numbers(self):
        result = self.bn.sum("12345678901234567890", "98765432109876543210")
        self.assertEqual(result, "111111111011111111100")
    
    def test_zero_addition(self):
        self.assertEqual(self.bn.sum("0", "0"), "0")
        self.assertEqual(self.bn.sum("123", "0"), "123")
        self.assertEqual(self.bn.sum("0", "456"), "456")
    
    def test_different_lengths(self):
        self.assertEqual(self.bn.sum("100", "200"), "300")
        self.assertEqual(self.bn.sum("1", "999999"), "1000000")
        self.assertEqual(self.bn.sum("123456", "7"), "123463")
    
    def test_single_digit(self):
        self.assertEqual(self.bn.sum("5", "3"), "8")
        self.assertEqual(self.bn.sum("9", "9"), "18")
    
    def test_multiple_carries(self):
        self.assertEqual(self.bn.sum("9999", "1"), "10000")
        self.assertEqual(self.bn.sum("888", "222"), "1110")
    
    def test_symmetric_addition(self):
        result1 = self.bn.sum("1234", "5678")
        result2 = self.bn.sum("5678", "1234")
        self.assertEqual(result1, result2)
    
def run_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestMyBigNumber))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())