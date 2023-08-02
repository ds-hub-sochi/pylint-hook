from setuptools import setup, find_packages

setup(
    name='pylint-hook',
    version='1.0.0',
    description='Pylint git hook with score',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pylint-hook=pkg.main:main',
        ],
    },
    install_requires=[
        'pylint',
    ],
)