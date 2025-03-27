from typing import Tuple
import math

def manhattan(pos: Tuple[int, int], goal: Tuple[int, int]) -> int:
    """Manhattan distance heuristic"""
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
