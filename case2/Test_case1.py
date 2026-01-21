import pytest


@pytest.fixture(scope='function', autouse=True)
def setup_and_teardown():
    """用于初始化数据和清理现场"""
    # 测试前执行
    print("setup")
    yield
    # 测试后执行
    print("teardown")


def test_1():
    # 测试代码
    print('第1条用例')


def test_2(setup_and_teardown):
    # 测试代码
    print('第2条用例')


class Test1:

    def test_3(self, setup_and_teardown):
        # 测试代码
        print('第3条用例')

    def test_4(self):
        # 测试代码
        print('第4条用例')

    def test_5(self):
        # 测试代码
        print('第5条用例')
