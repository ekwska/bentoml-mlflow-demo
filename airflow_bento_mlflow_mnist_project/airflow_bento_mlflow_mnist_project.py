"""Main module."""
from __future__ import print_function
import torch

from mnist import parse_args, create_train_test_loaders, Net, train, test


def main():
    args, kwargs = parse_args()
    torch.manual_seed(args.seed)
    if args.cuda:
        torch.cuda.manual_seed(args.seed)

    training_loader, testing_loader = create_train_test_loaders(args, kwargs)
    model = Net()
    if args.cuda:
        model.cuda()

    for epoch in range(1, args.epochs + 1):
        train(model, args, epoch, training_loader)
        test(model, args, testing_loader)


if __name__ == "__main__":
    main()
