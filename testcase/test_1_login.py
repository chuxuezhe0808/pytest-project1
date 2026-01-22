import pytest
import allure


@allure.story('登录')
@allure.title('使用正确账号+正确密码登录')
@allure.step('1、输入正确的账号'
             '2、输入正确的密码'
             '3、点击登录按钮')
def test1():
    print(f'登录1')


@allure.story('登录')
@allure.title('使用正确账号+错误密码登录')
def test2():
    print(f'登录2')


@allure.story('登录')
@allure.title('使用空账号+正确密码登录')
def test3():
    print(f'登录3')


@allure.story('登录')
@allure.title('使用空账号+正确密码登录')
def test4():
    print(f'登录4')
    assert 1 == 1


@allure.story('登录')
@allure.title('使用空账号+正确密码登录')
def test5():
    print(f'登录5')


@allure.story('登录')
@allure.title('使用空账号+正确密码登录')
def test6():
    print(f'登录6')
    assert 1 == 1


@allure.story('登录')
@allure.title('使用空账号+正确密码登录')
def test7():
    print(f'登录7')
    assert 1 == 1
