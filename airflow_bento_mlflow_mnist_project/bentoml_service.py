import bentoml
from bentoml.io import Image as BMLImage
from bentoml.io import NumpyNdarray
from torchvision import transforms
from typing import Any

from numpy.typing import NDArray
import numpy as np


def create_service(service_name, runner):
    svc = bentoml.Service(service_name, runners=[runner])

    @svc.api(input=BMLImage(), output=NumpyNdarray(dtype="float32"))
    async def predict_image(f: BMLImage) -> NDArray[Any]:
        # TODO: The image is empty here so predictions can't be made, investigate.
        transform = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        )
        arr = np.array(transform(f))
        assert arr.shape == (1, 28, 28)

        # We are using greyscale image and our PyTorch model expect one
        # extra channel dimension
        return await runner.async_run(arr)

    return svc


mnist_runner = bentoml.pytorch.get("23-09-23-16_39_mnist:oc5oqas2e6jhsblo").to_runner()
svc = create_service("mnist_service", mnist_runner)
