import hello


def test_hello_world(capfd):
    hello.hello_world()
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"
