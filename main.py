import pygame

from read_input import read_maze_from_file
from game_engine import GameEngine

INPUT_PATH = 'input.txt'
HEURISTIC_NAME = 'manhattan'
# ALGO_NAME = 'astar_ghost'
ALGO_NAME = 'bfs_ghost'

if __name__ == "__main__":
    pygame.init()

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    TILE_SZ = 10

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    # Initialize clock
    clock = pygame.time.Clock()
    FPS = 10

    # Initialize screen
    background = pygame.image.load('./assets/background.png')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Pathfinding")

    maze, start, goal = read_maze_from_file(INPUT_PATH)

    MAZE_WIDTH, MAZE_HEIGHT = len(maze[0]) * TILE_SZ, len(maze) * TILE_SZ
    DELTA_X = (SCREEN_WIDTH - MAZE_WIDTH) / 2
    DELTA_Y = (SCREEN_HEIGHT - MAZE_HEIGHT) / 2

    for algo in [ALGO_NAME]:
        game = GameEngine(algo, maze, start, goal, HEURISTIC_NAME)
        path: list[tuple[tuple[int, int], str]] = game.run()

        if path is None:
            print("No path found")
            exit(1)

        print("Path found")
        print(path)
        # Mark path cells in the maze
        for move in path:
            maze[move[0][0]][move[0][1]] = '*'

        maze[game.game_state["ghost_position"][0]][game.game_state["ghost_position"][1]] = 'G'
        maze[game.game_state["player_position"][0]][game.game_state["player_position"][1]] = 'P'

    path_to_animate = path[1:]  # Exclude the starting point
    current_path_index = 0

    # Pre-render the maze to a surface
    maze_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    maze_surface.blit(background, (0, 0))

    # Draw the static maze elements (walls, goal, player)
    for row_id, row in enumerate(maze):
        for col_id, cell in enumerate(row):
            x, y = col_id * TILE_SZ + DELTA_X, row_id * TILE_SZ + DELTA_Y
            if cell == 'x':
                pygame.draw.rect(maze_surface, WHITE, (x, y, TILE_SZ, TILE_SZ))
            elif cell == 'G':
                pygame.draw.rect(maze_surface, BLUE, (x, y, TILE_SZ, TILE_SZ))
            elif cell == 'P':
                pygame.draw.rect(maze_surface, BLACK, (x, y, TILE_SZ, TILE_SZ))

    running = True
    animation_complete = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the pre-rendered maze
        screen.blit(maze_surface, (0, 0))

        # Draw the path
        for i in range(current_path_index):
            row, col = path_to_animate[i][0]
            x, y = col * TILE_SZ + DELTA_X, row * TILE_SZ + DELTA_Y
            pygame.draw.rect(screen, GREEN, (x, y, TILE_SZ, TILE_SZ))

        # Advance the animation
        if current_path_index < len(path_to_animate):
            current_path_index += 1

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()