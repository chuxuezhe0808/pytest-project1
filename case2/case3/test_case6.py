import pytest


# @pytest.fixture
def my_info():
    info = {
        'name': 'zhangsan',
        'age': '16',
        'sex': '男'
    }
    print('个人信息为：', info)
    return info


# @pytest.mark.parametrize('name', ['张三', '李四', '王五'])
# def test_name(name):
#     print('开始测试test_name')
#     assert name == '李四'
#
# def test_age(test_my_info):
#     assert test_my_info['age'] == '16'
#
# def test_sex(test_my_info):
#     assert test_my_info['sex'] == '男'

import pytest


# 定义fixture
@pytest.fixture
def user_data(request):
    # request.param 包含参数化的值
    data = {
        "username": request.param[0],
        "age": request.param[1],
        "active": request.param[2]
    }
    return data


# 间接参数化
@pytest.mark.parametrize("user_data", [
    ("Alice", 25, True),
    ("Bob", 30, True),
    ("Charlie", 17, False)
], indirect=True)
def test_user_status(user_data):
    print(f"用户: {user_data['username']}, 年龄: {user_data['age']}")

    if user_data["age"] >= 18:
        assert user_data["active"] == True, "成年人应该激活"
    else:
        assert user_data["active"] == False, "未成年人应该未激活"


if __name__ == "__main__":
    # pytest.main(['test100.py'])                # 执行全部模块用例
    pytest.main(['-q', '-s', 'test_case6.py'])

