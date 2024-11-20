from abc import ABC, abstractmethod
from typing import Dict
from speech_box.config.config import Config


class Elstimator(ABC):
    def __init__(
        self,
        cfg: Config,
    ):
        pass

    @abstractmethod
    def model_info() -> Dict:
        pass
