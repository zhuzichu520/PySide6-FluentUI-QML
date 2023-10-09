import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = "PySide6-FluentUI-QML",
    version = "1.0.0",
    keywords="pyside fluent qml",
    author="ZhuZiChu",
    author_email="zhuzichu520@outlook.com",
    description="A fluent design qml library based on PySide6",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/zhuzichu520/FluentUI",
    packages=setuptools.find_namespace_packages(
                     include=["FluentUI", "FluentUI.*"], ),
    include_package_data=True,
    install_requires=[
        "PySide6>=6.5.0"
    ],
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
