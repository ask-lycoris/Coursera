### Concepts
# Unittest relies on the following concepts:
# Test fixture: This refers to preparing to perform one or more tests. In addition, test fixtures also include any actions involved in testing cleanup. This could involve creating temporary or proxy databases, directories, or starting a server process.
# Test case: This is the individual unit of testing that looks for a specific response to a set of inputs. If needed, TestCase is a base class provided by unittest and can be used to create new test cases.
# Test suite: This is a collection of test cases, test suites, or a combination of both. It is used to compile tests that should be executed together.
# Test runner: This runs the test and provides developers with the outcome’s data. The test runner can use different interfaces, like graphical or textual, to provide the developer with the test results. It can also provide a special value to developers to communicate the test results. 

# sample1: Cake factory
# from typing import List

# class CakeFactory:
#  def __init__(self, cake_type: str, size: str):
#    self.cake_type = cake_type
#    self.size = size
#    self.toppings = []
   
#    # Price based on cake type and size
#    self.price = 10 if self.cake_type == "chocolate" else 8
#    self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0

#  def add_topping(self, topping: str):
#      self.toppings.append(topping)
#      # Adding 1 to the price for each topping
#      self.price += 1

#  def check_ingredients(self) -> List[str]:
#      ingredients = ['flour', 'sugar', 'eggs']
#      ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
#      ingredients += self.toppings
#      return ingredients

#  def check_price(self) -> float:
#      return self.price

# # Example of creating a cake and adding toppings
# cake = CakeFactory("chocolate", "medium")
# cake.add_topping("sprinkles")
# cake.add_topping("cherries")
# cake_ingredients = cake.check_ingredients()
# cake_price = cake.check_price()
# cake_ingredients, cake_price

# 上記のコードに対するunittest
import unittest

class TestCakeFactory(unittest.TestCase):
 def test_create_cake(self):
   cake = CakeFactory("vanilla", "small")
   self.assertEqual(cake.cake_type, "vanilla")
   self.assertEqual(cake.size, "small")
   self.assertEqual(cake.price, 8) # Vanilla cake, small size

 def test_add_topping(self):
     cake = CakeFactory("chocolate", "large")
     cake.add_topping("sprinkles")
     self.assertIn("sprinkles", cake.toppings)

 def test_check_ingredients(self):
     cake = CakeFactory("chocolate", "medium")
     cake.add_topping("cherries")
     ingredients = cake.check_ingredients()
     self.assertIn("cocoa", ingredients)
     self.assertIn("cherries", ingredients)
     self.assertNotIn("vanilla extract", ingredients)

 def test_check_price(self):
     cake = CakeFactory("vanilla", "large")
     cake.add_topping("sprinkles")
     cake.add_topping("cherries")
     price = cake.check_price()
     self.assertEqual(price, 13) # Vanilla cake, large size + 2 toppings


# Running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))
