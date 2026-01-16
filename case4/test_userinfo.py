import pytest


# @pytest.fixture(scope="module")
def test_userInfo():

    info = {
        'name': 'zhangsan',
        'age': '16'
    }
    print(info)
    # return info
