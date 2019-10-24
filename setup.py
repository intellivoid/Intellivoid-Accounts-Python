from setuptools import setup, Extension

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='intellivoid_accounts',
    version='1.0.0',
    description='Intellivoid Accounts COA Wrapper for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['intellivoid_accounts'],
    package_dir={
        'intellivoid_accounts': 'intellivoid_accounts'
    },
    author='Zi Xing',
    author_email='netkas@intellivoid.info',
    url='https://accounts.intellivoid.info/',
    install_requires=[
        'requests>=2.3.0', 'six'
    ]
)
