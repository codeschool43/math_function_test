try:
    from math_func02 import main
except ImportError:
    assert False, "Not found"
    # def01 = lambda: None
#Create test to check import def01

#Create a test function to test the def01 function
def test_main_1():
    test = main(10)
    assert test == 62.83, "main is not answer"

def test_main_2():
    test = main(4)
    assert test == 25.13, "main is not answer"