==================================
bentoml_mlflow_demo
==================================

A project to run a full end to end ML system, using MLFlow for tracking, and BentoML for packaging and serving.


* Free software: MIT license

Features
--------

* Trains a model on the MNIST dataset to classify images of handwritten digits.
* Uses MLFlow as a backend tracking server to log metrics, parameters and models for development.
* Deploys a containerized bento of the trained model to serve predictions.

Installation
------------

Development
###########

System dependencies
*******************

- Python 3.10 or higher
- Docker
- BentoML
- Virtual environment
- Poetry

Steps
*****

1. Install the project in development mode with :code:`make install`
2. In a seperate terminal, run :code:`make run_mlflow_server` to spin up a locally served MLFLow server.
3. In your browser, open http://localhost:8080 and you should see the MLFlow tracking server running.
4. Run a training session with :code:`make train`
5. Test out the server with :code:`make serve`
6. Containerize the model using BentoML with :code:`make containerize`


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
