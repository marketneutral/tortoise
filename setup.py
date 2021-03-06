from setuptools import setup, find_packages

setup(
    name='tortoise',
    version='0.70',
    description='A Python machine learning library for tabular data, based on fastai v0.70',
    author='Jonathan Larkin',
    author_email='jonathan.r.larkin@gmail.com',
    packages=find_packages(exclude=('tests', 'docs'))
)
