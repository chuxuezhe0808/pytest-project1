import pytest


class Test1name:
    @pytest.mark.level1
    def test_11(self):
        print('第11条用例')
        assert 1 == 2

    @pytest.mark.level1
    @pytest.mark.level2
    def test_12(self):
        print('第12条用例')
        assert 1 == 1


class Test2name:

    @pytest.mark.level2
    def test_21(self):
        print('第21条用例')
        assert 1 == 1

    @pytest.mark.level2
    def test_22(self):
        print('第22条用例')
        assert 1 == 1