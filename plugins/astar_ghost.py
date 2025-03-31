import heapq
from typing import Optional, List, Tuple, Dict

from plugins.ghost_base import GhostBase


class astarGhost(GhostBase):
    def move(self, game_state) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        start: Tuple[int, int] = game_state["ghost_position"]
        goal: Tuple[int, int] = game_state["player_position"]

        if start == goal:
            return [(start, "NOT MOVING")]

        traced_path: Dict[Tuple[int, int], Tuple[Tuple[int, int], str]] = {}

        # just use the List and let the heapq manage the Priority Queue
        frontier: List[Tuple[int, Tuple[int, int]]] = [(0, start)]
        explored = set()

        cost_so_far: Dict[Tuple[int, int], int] = {start: 0}

        while frontier:
            _, position = heapq.heappop(frontier)

            if position in explored:
                continue
            explored.add(position)

            # goal reached → reconstruct the path
            if position == goal:
                path: List[str] = []
                actions: List[Tuple[int, int]] = []

                while position != start:
                    prev_position, direction = traced_path[position]
                    actions.append(prev_position)
                    path.append(direction)
                    position = prev_position

                actions.reverse()
                path.reverse()
                return list(zip(actions, path))

            # explore neighbors
            for neighbor in game_state["get_neighbors"](position):
                new_cost = cost_so_far[position] + 1

                if new_cost < cost_so_far.get(neighbor, float("inf")):
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + \
                               game_state["heuristic"](neighbor, goal)
                    heapq.heappush(frontier, (priority, neighbor))

                    if neighbor[0] == position[0]:
                        traced_path[neighbor] = (
                            position, "r" if neighbor[1] > position[1] else "l")
                    else:
                        traced_path[neighbor] = (
                            position, "d" if neighbor[0] > position[0] else "u")

        return None
