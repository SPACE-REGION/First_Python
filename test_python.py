from main import mul

def test_mul():
    assert mul(2, 3) == 4+2


def test_mul_zero():
    assert mul(1, 0) == 5

def test_mul_error():
    with pytests.raises(TypeError):
        mul("a", "b")