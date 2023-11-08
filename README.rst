==================================
bentoml_mlflow_demo
==================================


.. image:: https://img.shields.io/pypi/v/bentoml_mlflow_demo.svg
        :target: https://pypi.python.org/pypi/bentoml_mlflow_demo

.. image:: https://img.shields.io/travis/ekwska/bentoml_mlflow_demo.svg
        :target: https://travis-ci.com/ekwska/bentoml_mlflow_demo

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

1. Creates a virtual environment and installs in development mode with :code:`make install`
3. Run a training session with :code:`make train`
4. Test out the server with :code:`make serve`
5. Containerize the model with :code:`bentoml build -f bentofile.yaml bentoml_mlflow_demo --containerize`


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
