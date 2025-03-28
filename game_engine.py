from ghost_manager import GhostManager
from heuristic.heuristic_manager import HeuristicManager
from read_input import read_maze_from_file, print_maze
from typing import List, Tuple
import math


class GameEngine:
    def __init__(
        self,
        name: str,
        maze: list[list[str]],
        start: Tuple[int, int],
        goal: Tuple[int, int],
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

    def run(self) -> List[Tuple[Tuple[int, int], str]]:
        path = self.ghost_ai.move_ghost(self.game_state)

        return path


if __name__ == "__main__":
    maze, start, goal = read_maze_from_file("input.txt")

    for algo in ['bfs_ghost', 'astar_ghost']:
        game = GameEngine(algo, maze, start, goal, 'manhattan')

        path = game.run()

        if path is None:
            print("No path found")
            exit(1)

        print("Path found")
        # print(path)
        for move in path:
            # print(f"Ghost moves to {move[0]} with action {move[1]}")
            maze[move[0][0]][move[0][1]] = '*'

        maze[game.game_state["ghost_position"][0]
            ][game.game_state["ghost_position"][1]] = 'G'
        maze[game.game_state["player_position"][0]
            ][game.game_state["player_position"][1]] = 'P'

        # with open("output_bfs.txt", "w") as f:
        with open(f"output_{algo}.txt", "w") as f:
            for row in maze:
                f.write(''.join(row) + '\n')
            f.write('\nPath cost: ' + str(len(path)))
