import os

# 项目根目录
root = os.getcwd()

# 定义所有要创建的目录
folders = [
    "src",
    "src/strategy",
    "src/data",
    "src/backtest",
    "src/utils",
    "config",
    "logs",
    "output",
    "docs",
    "tests"
]

# 定义要创建的py文件
files = [
    "src/__init__.py",
    "src/strategy/__init__.py",
    "src/strategy/demo_strategy.py",
    "src/data/__init__.py",
    "src/data/fetch_data.py",
    "src/backtest/__init__.py",
    "src/backtest/engine.py",
    "src/utils/__init__.py",
    "src/utils/tools.py",
    "config/settings.yaml",
    "main.py",
    "requirements.txt",
    "README.md"
]

# 创建文件夹
for f in folders:
    path = os.path.join(root, f)
    os.makedirs(path, exist_ok=True)
    print(f"已创建目录：{path}")

# 创建空文件
for f in files:
    path = os.path.join(root, f)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as fp:
            fp.write("")
        print(f"已创建文件：{path}")
    else:
        print(f"文件已存在，跳过：{path}")

print("\n✅ 项目目录结构生成完成！")

