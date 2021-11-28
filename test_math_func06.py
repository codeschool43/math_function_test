try:
    from math_func06 import main
except ImportError:
    assert False, "Not found"
    # def01 = lambda: None
#Create test to check import def01

#Create a test function to test the def01 function
def test_main_1():
    test = main(4, 39)
    assert test == 3.24, "main is not answer"