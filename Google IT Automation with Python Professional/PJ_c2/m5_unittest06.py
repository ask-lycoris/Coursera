# Let's practice!! Below we have some code that makes a list of specific letters found in any string. If you run it, you can see what it does.
# visit here: https://www.coursera.org/learn/python-operating-system/ungradedLab/TZCyt/practice-notebook-unit-tests-and-edge-cases/lab?path=%2Fnotebooks%2FC2M5L2_Unit_Tests_and_Edge_Cases-V3.ipynb
import re
import unittest
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(___), ___)

unittest.main()
unittest.main(argv = ['first-arg-is-ignored'], exit = False)


class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
unittest.main(argv = ['first-arg-is-ignored'], exit = False)

