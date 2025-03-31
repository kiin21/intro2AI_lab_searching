from game_engine import GameEngine
from read_input import read_maze_from_file

INPUT_PATH = 'input.txt'
# HEURISTIC_NAME = 'manhattan'
HEURISTIC_NAME = 'euclidean'
# ALGO_NAME = 'astar_ghost'
ALGO_NAME = 'bfs_ghost'

if __name__ == "__main__":
    maze, start, goal = read_maze_from_file(INPUT_PATH)

    game = GameEngine(ALGO_NAME, maze, start, goal, HEURISTIC_NAME)

    game.run()