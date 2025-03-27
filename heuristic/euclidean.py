from typing import Tuple
import math

def euclidean(pos: Tuple[int, int], goal: Tuple[int, int]) -> int:
    """Euclidean distance heuristic"""
    return math.sqrt((pos[0] - goal[0])**2 + (pos[1] - goal[1])**2)
