from typing import Callable, Tuple, Optional
from heuristic.euclidean import euclidean
from heuristic.manhattan import manhattan

class HeuristicManager:
    def __init__(self, name: str):
        self.name = name
        self.heuristics: dict[str, Callable[[Tuple[int, int], Tuple[int, int]], int]] = {
            "euclidean": euclidean,
            "manhattan": manhattan
        }

    def get_heuristic(self, name: str) -> Optional[Callable[[Tuple[int, int], Tuple[int, int]], int]]:
        return self.heuristics.get(name.lower(), None)  # return none if not found