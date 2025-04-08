from typing import Optional, List, Tuple, Dict
from plugins.ghost_base import GhostBase

class dfsGhost(GhostBase):
    def move(self, game_state) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        start: Tuple[int, int] = game_state["ghost_position"]
        goal: Tuple[int, int] = game_state["player_position"]

        if start == goal:
            return [((start[0], start[1]), "NOT MOVING")]

        traced_path: Dict[Tuple[int, int], Tuple[Tuple[int, int], str]] = {}

        stack = [start]
        explored = {start}

        while stack:
            position = stack.pop()

            if position == goal:
                actions: List[str] = []
                path: List[Tuple[int, int]] = []

                while position != start:
                    prev_position, direction = traced_path[position]
                    path.append(prev_position)
                    actions.append(direction)
                    position = prev_position

                actions.reverse()
                path.reverse()
                return list(zip(path, actions))

            for neighbor in reversed(game_state["get_neighbors"](position)):
                if neighbor in explored:
                    continue

                # Store direction for path reconstruction
                if neighbor[0] == position[0]:
                    traced_path[neighbor] = (position, "r" if neighbor[1] > position[1] else "l")
                else:
                    traced_path[neighbor] = (position, "d" if neighbor[0] > position[0] else "u")

                stack.append(neighbor)
                explored.add(neighbor)

        return None
