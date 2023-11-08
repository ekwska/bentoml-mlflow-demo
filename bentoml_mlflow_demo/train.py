"""Module to run CNN training from."""

from __future__ import print_function
import torch
import mlflow
import os
import logging
from bentoml_mlflow_demo.mnist import (
    Net,
    train,
    test,
    save_bentoml_model,
)

from bentoml_mlflow_demo.utils import (
    parse_args,
    create_train_test_loaders,
    log_mlflow_hyperparameters,
)


logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=logging.INFO
)


def main() -> None:
    """Run training of a simple CNN and save it in BentoML model format, using
     CLI arguments to control the hyperparameters.

    Returns: None
    """
    args, kwargs = parse_args()
    torch.manual_seed(args.seed)
    if args.cuda:
        torch.cuda.manual_seed(args.seed)

    training_loader, testing_loader = create_train_test_loaders(args, kwargs)
    model = Net()
    if args.cuda:
        model.cuda()

    # Setup MLFlow
    mlflow.set_tracking_uri("http://127.0.0.1:8080")
    mlflow.set_experiment("MNIST BentoML Demo Experiment")

    # Begin training
    mlflow.start_run()
    log_mlflow_hyperparameters(args)
    for epoch in range(1, args.epochs + 1):
        model = train(model, args, epoch, training_loader)
        test(model, args, testing_loader, epoch)
    mlflow.pytorch.log_model(model, artifact_path="mnist_classifier")
    logging.info(
        f"Model logged at: {os.path.join(mlflow.get_artifact_uri(), 'mnist_classifier')}"
    )
    mlflow.end_run()
    save_bentoml_model(model)


if __name__ == "__main__":
    main()
