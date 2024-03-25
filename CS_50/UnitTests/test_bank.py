import bank
from bank import value
def main():
    test_bank()
    
def test_bank():
    assert value('hello') == 0
    assert value('hi') == 20
    assert value('bye') == 100    
main()    