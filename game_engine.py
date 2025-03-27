from ghost_manager import GhostManager
from read_input import read_maze_from_file, print_maze
from typing import List, Tuple
import math

class GameEngine:
    def __init__(self, name: str, maze: list[list[str]], start: Tuple[int, int], goal: Tuple[int, int]):
        self.ghost_ai = GhostManager(name)
        self.game_state = {
            "ghost_position": start,
            "player_position": goal,
            "get_neighbors": self.get_neighbors,
            "heuristic": self.heuristic
        }
        self.maze = maze

    def get_neighbors(self, pos):
        x, y = pos
        res = []
        for(dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < len(self.maze) and 0 <= y + dy < len(self.maze[0]):
                if self.maze[x + dx][y + dy] != 'x':
                    res.append((x + dx, y + dy))
        return res

    def heuristic(self, pos, goal) -> int:
        # """Manhattan distance heuristic"""
        # return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
        """Euclidean distance heuristic"""
        return math.sqrt((pos[0] - goal[0])**2 + (pos[1] - goal[1])**2)

    def run(self) -> List[Tuple[Tuple[int, int], str]]:
        """Main game loop"""
        path = self.ghost_ai.move_ghost(self.game_state)

        return path

if __name__ == "__main__":
    maze, start, goal = read_maze_from_file("input.txt")

    game = GameEngine("bfs_ghost", maze, start, goal)

    # game = GameEngine("astar_ghost", maze, start, goal)


    path = game.run()

    if path is None:
        print("No path found")
        exit(1)

    print("Path found:")
    # print(path)
    for move in path:
        # print(f"Ghost moves to {move[0]} with action {move[1]}")
        maze[move[0][0]][move[0][1]] = '*'

    maze[game.game_state["ghost_position"][0]][game.game_state["ghost_position"][1]] = 'G'
    maze[game.game_state["player_position"][0]][game.game_state["player_position"][1]] = 'P'

    with open("output_bfs.txt", "w") as f:
    # with open("output_astar.txt", "w") as f:
        for row in maze:
            f.write(''.join(row) + '\n')
        f.write('\nPath cost: ' + str(len(path)))
    
