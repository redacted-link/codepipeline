from app import hello
def test_app():
    assert hello()=="hello"

def test_app_fail():
    assert hello()!="hello"