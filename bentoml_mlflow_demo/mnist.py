"""
CNN model code to run a simple classification and allow for saving in BentoML format.
"""

from __future__ import print_function
import argparse
import logging
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from bentoml.pytorch import save_model
from datetime import datetime


class Net(nn.Module):
    """
    A simple convolutional network for classifying MNIST images.
    """

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x)


def train(
    model: Net,
    args: argparse.ArgumentParser,
    train_epoch: int,
    train_loader: torch.utils.data.DataLoader,
) -> Net:
    """Run a single epoch of training of the MNIST model.

    Args:
        model: Torch model object to run training with.
        args: Argument parser to set hyperparameters with.
        train_epoch: Current training epoch.
        train_loader: Training data loader of the validation set.

    Returns: MNIST model trained for a single epoch.

    """
    logging.info("Training model")
    train_optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data), Variable(target)
        train_optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        train_optimizer.step()
        if batch_idx % args.log_interval == 0:
            logging.info(
                "Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}".format(
                    train_epoch,
                    batch_idx * len(data),
                    len(train_loader.dataset),
                    100.0 * batch_idx / len(train_loader),
                    loss.data.item(),
                )
            )
    return model


def test(
    model: Net, args: argparse.ArgumentParser, test_loader: torch.utils.data.DataLoader
) -> None:
    """Run validation of a model using a test data loader.

    Args:
        model: Torch model object to run training with.
        args: Argument parser to set hyperparameters with.
        test_loader: Testing data loader of the validation set.

    Returns: None

    """
    logging.info("Testing model")
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        test_loss += F.nll_loss(
            output, target, size_average=False
        ).data.item()  # sum up batch loss
        pred = output.data.max(1)[1]  # get the index of the max log-probability
        correct += pred.eq(target.data).cpu().sum()

    test_loss /= len(test_loader.dataset)
    logging.info(
        "\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n".format(
            test_loss,
            correct,
            len(test_loader.dataset),
            100.0 * correct / len(test_loader.dataset),
        )
    )


def save_bentoml_model(model: Net) -> None:
    """Save a trained model in bentoML format.

    Args:
        model: Trained MNIST model.

    Returns: None.

    """
    model_name = datetime.now().strftime("mnist")
    save_model(model_name, model)
    logging.info(f"Model saved under name '{model_name}'")
