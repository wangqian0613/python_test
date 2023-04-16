import pytest

data_dict = [
    {"case": 1, "title": "login in success"},
    {"case": 2, "title": "login in fail"},
]


class TestLogin:
    @pytest.mark.parametrize("item", data_dict)
    def test_login_001(self, item):
        print(item)
