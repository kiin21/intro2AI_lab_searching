from typing import List, Tuple, Optional
from abc import ABC, abstractmethod

class GhostAIBase(ABC):
    @abstractmethod
    def move(self, game_state) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        pass
