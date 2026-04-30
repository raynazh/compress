# 测试用例
test_cases = [
    "BBBUYSELLL",
    "AAABBC",
    "AGGGJKKIYYYYJJIFFFFJ",
    "BB",
    "UUU",
    "ABCD",
    "AABBBCCCC",
    "Z" * 100   # 100个Z
]

from demo1 import compress_string  # 假设从上面代码导入

for s in test_cases:
    compressed = compress_string(s)
    print(f"输入：{s:20} → 输出：{compressed}")