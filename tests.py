import unittest
from solutions import pairs, is_four_of_kind, merge, dec_to_base_x
 

class SolutionsTests(unittest.TestCase):

    def test_not_four_of_kind(self):
        alpha = ["J", "Q", "K", "A"]
        num_list = list(range(2,11))
        for x in num_list:
            x = str(x)
            if x != "5":
                self.assertTrue(is_four_of_kind([x, x, x, x, "5"]))
                self.assertTrue(is_four_of_kind([x, x, x, "5", x]))
                self.assertTrue(is_four_of_kind([x, "5", x, x, x]))
                self.assertTrue(is_four_of_kind([x, x, "5", x, x]))
                self.assertTrue(is_four_of_kind(["5", x, x, x, x]))
        for x in alpha:
            x = str(x)
            self.assertTrue(is_four_of_kind([x, x, x, x, "5"]))
            self.assertTrue(is_four_of_kind([x, x, x, "5", x]))
            self.assertTrue(is_four_of_kind([x, "5", x, x, x]))
            self.assertTrue(is_four_of_kind([x, x, "5", x, x]))
            self.assertTrue(is_four_of_kind(["5", x, x, x, x]))
 
 
if __name__ == '__main__':
    unittest.main()
