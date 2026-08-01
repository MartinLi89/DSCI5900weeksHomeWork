#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from pathlib import Path

# 步骤 1： 中文伪代码：
# 1 创建一个名为 inventory 的列表。
#       在列表中加入 3 个商品，每个商品都是一个字典。
#       每个商品字典包含 name、quantity 和 price 三个键。


# 2 创建一个名为 calculate_total_value() 的函数。
#       在函数中创建 total_value，并设置为 0。
#       遍历 inventory 中的每一个商品。
#           用商品的 quantity 乘以 price，计算该商品的库存价值。
#           将每个商品的库存价值加到 total_value 中。
#       返回 total_value。
# 3 创建 main() 函数。
#       在 main() 中调用 calculate_total_value() 函数。
#       打印最终库存总价值。
#       如果当前文件是直接运行的程序，则调用 main() 函数。

# 步骤 2：转换为 Python 代码

inventory = [
    {"name": "Notebook", "quantity": 10, "price": 2.50},
    {"name": "Pen", "quantity": 25, "price": 1.20},
    {"name": "Backpack", "quantity": 5, "price": 29.99},
]


def calculate_total_value():
    total_value = 0

    for product in inventory:
        item_value = product["quantity"] * product["price"]
        total_value += item_value

    return total_value


# 步骤 3：测试你的代码。 测试伪代码：
# 1 创建 main() 函数。
#       在 main() 函数中调用 calculate_total_value()。
#       将返回的库存总价值保存到 final_total。
#       打印 final_total，显示当前库存的总价值。
# 2 创建 if __name__ == "__main__" 判断。
#       如果当前 Python 文件是被直接运行，则调用 main() 函数。
#       如果当前 Python 文件是被其他文件导入，则不自动运行 main() 函数。
# 3 创建测试用例，用于测试当前代码,coverage统计测试覆盖率>70。
#       测试用例 1：运行程序，检查输出是否为 Total inventory value: $204.95。
#       测试用例 2：手动计算 10 * 2.50 + 25 * 1.20 + 5 * 29.99。
#       比较程序输出结果和手动计算结果是否一致。
#       程序执行结束时，自动统计并打印当前代码测试覆盖率。


def test_calculate_total_value():
    expected_total = 10 * 2.50 + 25 * 1.20 + 5 * 29.99
    actual_total = calculate_total_value()

    assert round(actual_total, 2) == round(expected_total, 2)

    expected_output = "Total inventory value: $204.95"
    actual_output = f"Total inventory value: ${actual_total:.2f}"

    assert actual_output == expected_output
    print("All tests passed.")


def main():
    final_total = calculate_total_value()
    print(f"Total inventory value: ${final_total:.2f}")
    test_calculate_total_value()


def run_with_coverage():  # pragma: no cover
    coverage_env_var = "INVENTORY_VALUE_RUNNING_WITH_COVERAGE"

    if os.environ.get(coverage_env_var) == "1":
        main()
        return

    try:
        import coverage  # noqa: F401
    except ModuleNotFoundError:
        main()
        print("Coverage is not installed. Run: python -m pip install coverage")
        return

    env = os.environ.copy()
    env[coverage_env_var] = "1"
    script_path = Path(__file__).resolve()

    subprocess.run([sys.executable, "-m", "coverage", "erase"], check=True)
    subprocess.run(
        [sys.executable, "-m", "coverage", "run", str(script_path)],
        check=True,
        env=env,
    )
    subprocess.run(
        [sys.executable, "-m", "coverage", "report", "-m", str(script_path)],
        check=True,
    )


if __name__ == "__main__":
    run_with_coverage()
