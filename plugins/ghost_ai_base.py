from abc import ABC, abstractmethod
from typing import List, Tuple, Optional


class GhostAIBase(ABC):
    @abstractmethod
    def move(self, game_state) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        pass
