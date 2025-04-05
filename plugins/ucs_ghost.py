from collections import deque
from typing import Optional, List, Tuple, Dict

from plugins.ghost_base import GhostBase

class ucsGhost(GhostBase):
    def move(self, game_state) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        start: Tuple[int, int] = game_state["ghost_position"]
        goal: Tuple[int, int] = game_state["player_position"]

        if start == goal:
            return [(start, "NOT MOVING")]

        frontier = deque([start])
        explored = {start}
        traced_path: Dict[Tuple[int, int], Tuple[Tuple[int, int], str]] = {}

        while frontier:
            position = frontier.popleft()

            if position == goal:
                path: List[Tuple[int, int]] = []
                actions: List[str] = []
                while position != start:
                    prev, direction = traced_path[position]
                    path.append(position)
                    actions.append(direction)
                    position = prev
                path.reverse()
                actions.reverse()
                return list(zip(path, actions))

            directions = [
                ((0, 1), "r"),
                ((0, -1), "l"),
                ((-1, 0), "u"),
                ((1, 0), "d")
            ]

            for delta, dir_str in directions:
                neighbor = (position[0] + delta[0], position[1] + delta[1])

                if neighbor in explored:
                    continue

                if neighbor in game_state["get_neighbors"](position):
                    traced_path[neighbor] = (position, dir_str)
                    explored.add(neighbor)
                    frontier.append(neighbor)

        return None
