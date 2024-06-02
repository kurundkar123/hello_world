import hello

def test_hello_world(capfd):
    print("Test Passed")
    assert hello.hello_world() == "Hello, World!"
