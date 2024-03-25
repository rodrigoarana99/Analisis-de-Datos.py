import twttr
from twttr import shorten

def main():
    test_tweet()

def test_tweet():
    assert shorten('hola mundo') == 'hl mnd'

if __name__=="__main()__ ":
    main()  
