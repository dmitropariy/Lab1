import pytest

@pytest.fixture
def func():
    return 2

def add1(x):
    return x + 1

def main():
    print('Hello')

if __name__ == '__main__':
    main()