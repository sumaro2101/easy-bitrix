from setuptools import setup


setup(
    name='easy-bitrix',
    version='0.1.0',
    description='Python Library with easy API for Bitrix24 REST',
    author='Alexsander Pavlov',
    author_email='yukiu217@gmail.com',
    packages=['.'],
    install_requires=['httpx'],
)