from default_python.main import get_taxis, get_spark


def test_main():
    import os
    print(os.environ)
    taxis = get_taxis(get_spark())
    assert taxis.count() > 5
