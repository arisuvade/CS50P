from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Aries Dave") == "Ars Dv"
