from abc import ABC, abstractmethod
from typing import List, Tuple, Optional


class GhostBase(ABC):
    @abstractmethod
    def move(self, game_state) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        pass
