try:
    from math_func03 import main
except ImportError:
    assert False, "Not found"
    # def01 = lambda: None
#Create test to check import def01

#Create a test function to test the def01 function
def test_main_1():
    test = main(7)
    assert test == 49, "main is not answer"

def test_main_2():
    test = main(1.5)
    assert test == 2.25, "main is not answer"