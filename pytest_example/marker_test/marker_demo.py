import pytest


@pytest.mark.ok
class TestLogin:
    @pytest.mark.ok
    @pytest.mark.fail
    def test_001(self):
        assert 20 == 20

    @pytest.mark.ok
    @pytest.mark.passed
    def test_002(self):
        assert 100 == 100

    @pytest.mark.ok
    @pytest.mark.fail
    def test_003(self):
        assert 20 == 20

    @pytest.mark.passed
    @pytest.mark.success
    def test_004(self):
        assert 100 == 100

    @pytest.mark.skip
    @pytest.mark.success
    def test_005(self):
        assert 20 == 20


if __name__ == "__main__":
    pytest.main(["-m ok", "-s"])