from setuptools import setup, find_packages

setup(
    name='translateyoudao',         # 应用名
    version='1.0',        # 版本号
    packages=find_packages(exclude=['tests']),    # 包括在安装包内的Python包
    install_requires=[    # 依赖列表
        'selenium',
    ]
)
