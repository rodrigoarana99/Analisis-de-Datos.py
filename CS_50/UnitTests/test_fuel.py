import fuel
from fuel import convert,gauge
def main():
    test_convert()
    
    
def test_convert():
    assert convert("1/2") == 50
    assert gauge(int(50)) == "50%"
  
main()
