import os
import shutil
import pytest


@pytest.fixture(autouse=True, scope='session')
def copy_history_files_with_overwrite():
    """复制allure-report历史文件放到allure-xml中，实现allure趋势图，每次测试完成后执行1次"""
    yield
    project_root = os.path.dirname(os.path.abspath(__file__))
    # 定义目录路径
    src_dir = os.path.join(project_root, "allure-report", "history")
    dst_dir = os.path.join(project_root, "allure-xml", "history")

    # 检查源目录是否存在
    if not os.path.exists(src_dir):
        print(f"源目录不存在: {src_dir}")
        return False

    # 创建目标目录（如果不存在）
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print(f"创建目标目录: {dst_dir}")

    # 复制文件
    copied_count = 0
    skipped_count = 0
    error_count = 0

    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename)

        # 只处理文件，跳过子目录
        if os.path.isfile(src_file):
            try:
                # 使用 copy2 保留文件元数据（修改时间等）
                shutil.copy2(src_file, dst_file)
                copied_count += 1
                # print(f"✓ 已复制: {filename}")
            except PermissionError:
                # print(f"✗ 权限拒绝: {filename}")
                error_count += 1
            except Exception as e:
                # print(f"✗ 复制失败 {filename}: {e}")
                error_count += 1
        else:
            # print(f"- 跳过目录: {filename}")
            skipped_count += 1

    # 输出结果
    # print("\n" + "=" * 50)
    print(f"复制完成!")
    # print(f"成功复制: {copied_count} 个文件")
    # print(f"跳过目录: {skipped_count} 个")
    # print(f"失败文件: {error_count} 个")
    # print("=" * 50)

    return error_count == 0


