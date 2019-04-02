import pytest

@pytest.fixture(scope="module")
def cluster():
    yield 1


def test(cluster):
    print(cluster + 3)
