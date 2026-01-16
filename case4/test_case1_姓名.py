import pytest
# from case4.test_userinfo import test_userInfo


def test1(test_userInfo):

    assert test_userInfo['name'] == 'zhangsan'


if __name__ == "__main__":
    # pytest.main(['test100.py'])                # 执行全部模块用例
    pytest.main(['-q', '-s', 'test_case1_姓名.py'])
