from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING
from torchvision import transforms

import numpy as np
from PIL.Image import Image as PILImage

import bentoml

if TYPE_CHECKING:
    from numpy.typing import NDArray

mnist_runner = bentoml.pytorch.get("mnist:latest").to_runner()

svc = bentoml.Service(name="mnist_service", runners=[mnist_runner])


@svc.api(input=bentoml.io.Image(), output=bentoml.io.NumpyNdarray())
async def predict(f: PILImage) -> NDArray[t.Any]:
    arr = np.array(f) / 255.0
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
    )
    arr = np.array(transform(arr))
    arr = np.expand_dims(arr, (0, 3)).squeeze(3)
    res = await mnist_runner.async_run(arr)
    return res.argmax()
