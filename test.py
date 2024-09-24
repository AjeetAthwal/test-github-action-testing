from main import return_hello

def test_return_hello():
    str = "world"
    return_str = return_hello(str)

    assert return_str == "hello " + str