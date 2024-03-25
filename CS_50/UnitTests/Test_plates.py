import plates 
from plates import is_valid
def main():
    test_plates()

def test_plates():
    assert is_valid('cs50') == True
    assert is_valid('cs05') == False
    assert is_valid('hello, world') == False
main()    