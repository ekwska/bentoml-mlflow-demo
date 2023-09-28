==================================
airflow_bento_mlflow_mnist_project
==================================


.. image:: https://img.shields.io/pypi/v/airflow_bento_mlflow_mnist_project.svg
        :target: https://pypi.python.org/pypi/airflow_bento_mlflow_mnist_project

.. image:: https://img.shields.io/travis/ekwska/airflow_bento_mlflow_mnist_project.svg
        :target: https://travis-ci.com/ekwska/airflow_bento_mlflow_mnist_project

.. image:: https://readthedocs.org/projects/airflow-bento-mlflow-mnist-project/badge/?version=latest
        :target: https://airflow-bento-mlflow-mnist-project.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A project to run a full end to end ML system, using MLFlow for tracking, Airflow for pipeline construction and BentoML for packaging.


* Free software: MIT license
* Documentation: https://airflow-bento-mlflow-mnist-project.readthedocs.io.


Features
--------

* Trains a model on the MNIST dataset to classify images of handwritten digits.
* Deploys a containerized bento of the trained model to serve predictions.

Installation
------------

Development
###########

System dependencies
*******************

- Python 3.11
- Docker
- BentoML
- Virtual environment

Steps
*****

1. Create a virtual environment :code:`python3.11 -m venv .venv`
2. Activate the virtual environment with :code:`.venv/bin/activate`
2. Install the development packages with :code:`pip install -r requirements.txt`
3. Run a training session with :code:`python3 airflow_bento_mlflow_mnist_project/mnist.py`
4. Test out the server with :code:`bentoml serve bentoml_service.py:svc --working-dir airflow_bento_mlflow_mnist_project --reload`
5. Containerize the model with :code:`bentoml build -f bentofile.yaml airflow_bento_mlflow_mnist_project --containerize`


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
