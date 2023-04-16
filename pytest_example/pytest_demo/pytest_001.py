import pytest


def test_demo001():
    print("######## first_test ########")
    assert (1==1)


class TestDemo:
    def test_demo002(self):
        print("######## second_test ########")
        assert (2==1)


if __name__ == "__main__":
    pytest.main()