from setuptools import setup, find_packages

setup(
    name='translateyoudao',
    version='1.4',
    description='基于有道云web翻译接口的翻译工具包，无需有道云账号，设置动态代理后理论上可无限调用，详情请见github',
    long_description=('基于有道云web翻译接口的翻译工具包，无需有道云账号，设置动态代理后理论上可无限调用，'
                      '详情请见github'),
    author='simba',
    author_email='1531315@qq.com',
    maintainer='simba',
    maintainer_email='1531315@qq.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/px3303/translateyoudao',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[  # 依赖列表
        'requests',
    ]
)
