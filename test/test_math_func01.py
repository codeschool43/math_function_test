try:
    from math_func01 import main
except ImportError:
    assert False, "Not found"
    # def01 = lambda: None
#Create test to check import def01

#Create a test function to test the def01 function
def test_main_1():
    test = main(16)
    assert test == 4.0, "main is not answer"

def test_main_2():
    test = main(2.25)
    assert test == 1.5, "main is not answer"