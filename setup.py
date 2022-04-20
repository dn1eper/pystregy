from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pystregy',
    url='https://github.com/dnepr0/pystregy',
    author='Andrii Zadneprovskyi',
    author_email='andneprovskii@gmail.com',
    packages=['pystregy', 'pystregy.model', 'pystregy.goadapter'],
    install_requires=['stickytape', 'nose'],
    version='0.0.3',
    license='MIT',
    description='Python client for Stregy',
    long_description=long_description,
    scripts=['pystregy/trader.py'],
)