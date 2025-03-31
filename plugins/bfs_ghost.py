from collections import deque
from typing import Optional, List, Tuple, Dict

from plugins.ghost_ai_base import GhostAIBase


class bfsGhost(GhostAIBase):
    def move(self, game_state) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        start: Tuple[int, int] = game_state["ghost_position"]
        goal: Tuple[int, int] = game_state["player_position"]


        if start == goal:
            return [((start[0], start[1]), "NOT MOVING")]

        traced_path: Dict[Tuple[int, int], Tuple[Tuple[int, int], str]] = {}

        frontier = deque([start])
        explored = {start}

        while frontier:
            position = frontier.popleft()

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

            # Explore neighbors
            for neighbor in game_state["get_neighbors"](position):
                if neighbor in explored or neighbor in frontier:
                    continue

                # Store direction for path reconstruction
                if neighbor[0] == position[0]:
                    traced_path[neighbor] = (position, "r" if neighbor[1] > position[1] else "l")
                else:
                    traced_path[neighbor] = (position, "d" if neighbor[0] > position[0] else "u")

                frontier.append(neighbor)
                explored.add(neighbor)

        return None
