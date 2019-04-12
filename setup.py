from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_text = f.read()

setup(
    name='jtyoui',
    version='19.4.12',
    description='This is my collection bag.',
    long_description=long_text,
    url='https://github.com/jtyoui/Jtyoui',
    author='Jtyoui',
    author_email='jtyoui@qq.com',
    license='MIT Licence',
    packages=find_packages(),
    platforms=["window10"],
    package_data={'': ['*']},
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
