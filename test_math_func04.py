try:
    from math_func04 import main
except ImportError:
    assert False, "Not found"
    # def01 = lambda: None
#Create test to check import def01

#Create a test function to test the def01 function
def test_main_1():
    test = main(8, 27)
    assert test == 3.63, "main is not answer"