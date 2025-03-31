from ghost_manager import GhostManager
from heuristic.heuristic_manager import HeuristicManager


class GameEngine:
    def __init__(
        self,
        name: str,
        maze: list[list[str]],
        start: tuple[int, int],
        goal: tuple[int, int],
        heuristic_name: str = "Euclidean"
    ):
        self.ghost_ai = GhostManager(name)
        self.game_state = {
            "ghost_position": start,
            "player_position": goal,
            "get_neighbors": self.get_neighbors,
            "heuristic": HeuristicManager(heuristic_name).get_heuristic()
        }
        self.maze = maze

    def get_neighbors(self, pos):
        x, y = pos
        res = []
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < len(self.maze) and 0 <= y + \
                    dy < len(self.maze[0]):
                if self.maze[x + dx][y + dy] != 'x':
                    res.append((x + dx, y + dy))
        return res

    def run(self) -> list[tuple[tuple[int, int], str]]:
        path = self.ghost_ai.move_ghost(self.game_state)

        return path

