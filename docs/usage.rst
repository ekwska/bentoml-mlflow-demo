=====
Usage
=====

Development
###########

To run the project in development mode locally, follow the below steps:

1. Install the project in development mode with :code:`make install`
2. In a seperate terminal, run :code:`make run_mlflow_server` to spin up a locally served MLFLow server.
3. In your browser, open http://localhost:8080 and you should see the MLFlow tracking server running.
4. Run a training session with :code:`make train`
5. Test out the server with :code:`make serve`
6. Containerize the model using BentoML with :code:`make containerize`
