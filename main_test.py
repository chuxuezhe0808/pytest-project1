import pytest
import os


pytest.main(['testcase'])

os.system('allure generate allure-xml -o allure-report --clean')
