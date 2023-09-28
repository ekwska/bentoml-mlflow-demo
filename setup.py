#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["torch", "torchvision", "bentoml[io-image]", "Pillow", "numpy"]

test_requirements = ['pytest>=3', "black", "flake8"]

setup(
    author="ekwska",
    author_email='ekwska0@protonmail.com',
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    description="A project to run a full end to end ML system, using MLFlow for tracking, Airflow for pipeline construction and BentoML for packaging,",
    entry_points={
        'console_scripts': [
            'airflow_bento_mlflow_mnist_project=airflow_bento_mlflow_mnist_project.main:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='airflow_bento_mlflow_mnist_project',
    name='airflow_bento_mlflow_mnist_project',
    packages=find_packages(include=['airflow_bento_mlflow_mnist_project', 'airflow_bento_mlflow_mnist_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ekwska/airflow_bento_mlflow_mnist_project',
    version='0.1.0',
    zip_safe=False,
)
