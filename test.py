from main import func, add1
import pytest

def test_func(func):
    assert func == 2

@pytest.mark.parametrize(
    ('input', 'output'),
    (
            (1, 2),
            (-1, 0),
            (0, 1),
            (145, 146)
    )
)
def test_add1(input, output):
    assert add1(input) == output