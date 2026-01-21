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
