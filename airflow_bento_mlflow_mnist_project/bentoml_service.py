import bentoml
from bentoml.io import NumpyNdarray
import numpy as np


def create_service(service_name, runner):
    svc = bentoml.Service(service_name, runners=[runner])

    @svc.api(input=NumpyNdarray(), output=NumpyNdarray())
    def classify(input_series: np.ndarray) -> np.ndarray:
        result = runner.predict.run(input_series)
        return result

    return svc


mnist_runner = bentoml.pytorch.get("23-09-23-16_39_mnist:oc5oqas2e6jhsblo").to_runner()
svc = create_service("mnist_service", mnist_runner)
