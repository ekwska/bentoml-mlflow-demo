"""
Helper utility functions for running training and configuration management.
"""

from __future__ import print_function
import argparse
import logging
import mlflow
import torch
from torchvision import datasets, transforms
from typing import Tuple


def parse_args():
    parser = argparse.ArgumentParser(description="PyTorch MNIST Example")
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        metavar="N",
        help="input batch size for training (default: 64)",
    )
    parser.add_argument(
        "--test-batch-size",
        type=int,
        default=1000,
        metavar="N",
        help="input batch size for testing (default: 1000)",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=3,
        metavar="N",
        help="number of epochs to train (default: 2)",
    )
    parser.add_argument(
        "--lr",
        type=float,
        default=0.01,
        metavar="LR",
        help="learning rate (default: 0.01)",
    )
    parser.add_argument(
        "--momentum",
        type=float,
        default=0.5,
        metavar="M",
        help="SGD momentum (default: 0.5)",
    )
    parser.add_argument(
        "--no-cuda", action="store_true", default=True, help="disables CUDA training"
    )
    parser.add_argument(
        "--seed", type=int, default=1, metavar="S", help="random seed (default: 1)"
    )
    parser.add_argument(
        "--log-interval",
        type=int,
        default=10,
        metavar="N",
        help="how many batches to wait before logging training status",
    )
    parsed_args = parser.parse_args()
    parsed_args.cuda = not parsed_args.no_cuda and torch.cuda.is_available()
    kwargs = {"num_workers": 1, "pin_memory": True} if parsed_args.cuda else {}
    return parsed_args, kwargs


def create_train_test_loaders(
    args: argparse.ArgumentParser, kwargs: dict
) -> Tuple[torch.utils.data.DataLoader, torch.utils.data.DataLoader]:
    """Create train or test loaders using required parameters.

    Args:
        args: Argparse object - only the `batch_size` argument needs to be
         set to create the train/test data loaders.
        kwargs: Any additional keyword arguments to pass to the data loader
         initialization.

    Returns: Training loader and testing loader.

    """
    logging.info("Create train and test loaders...")
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            "../data",
            train=True,
            download=True,
            transform=transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
            ),
        ),
        batch_size=args.batch_size,
        shuffle=True,
        **kwargs,
    )
    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            "../data",
            train=False,
            transform=transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
            ),
        ),
        batch_size=args.batch_size,
        shuffle=True,
        **kwargs,
    )
    return train_loader, test_loader


def log_mlflow_hyperparameters(args: argparse.ArgumentParser) -> None:
    """Iteratively log parameters to an MLFLow tracking server
     in an argparser object.

    Args:
        args: Argument parser to extract parameters to log from.

    Returns: None

    """
    for arg in vars(args):
        mlflow.log_param(arg, getattr(args, arg))
