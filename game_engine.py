from ghost_manager import GhostManager
from heuristic.heuristic_manager import HeuristicManager
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

TILE_SZ = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

FPS = 10

class GameEngine:
    def __init__(
            self,
            algo_name: str,
            maze: list[list[str]],
            start: tuple[int, int],
            goal: tuple[int, int],
            heuristic_name: str = "Euclidean"
    ):
        self.ghost_ai = GhostManager(algo_name)
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

    def run(self):
        path = self.ghost_ai.move_ghost(self.game_state)

        if path is None:
            print("No path found")
            return None

        pygame.init()

        # Initialize clock
        clock = pygame.time.Clock()

        # Initialize screen
        background = pygame.image.load('./assets/background.png')
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Maze Pathfinding")

        MAZE_WIDTH, MAZE_HEIGHT = len(self.maze[0]) * TILE_SZ, len(self.maze) * TILE_SZ
        DELTA_X = (SCREEN_WIDTH - MAZE_WIDTH) / 2
        DELTA_Y = (SCREEN_HEIGHT - MAZE_HEIGHT) / 2

        # Mark path cells in the maze
        for move in path:
            self.maze[move[0][0]][move[0][1]] = '*'

        self.maze[self.game_state["ghost_position"][0]][self.game_state["ghost_position"][1]] = 'G'
        self.maze[self.game_state["player_position"][0]][self.game_state["player_position"][1]] = 'P'

        path_to_animate = path[1:]  # Exclude the starting point
        current_path_index = 0

        # Pre-render the maze to a surface
        maze_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        maze_surface.blit(background, (0, 0))

        # Draw the static maze elements (walls, goal, player)
        for row_id, row in enumerate(self.maze):
            for col_id, cell in enumerate(row):
                x, y = col_id * TILE_SZ + DELTA_X, row_id * TILE_SZ + DELTA_Y
                if cell == 'x':
                    pygame.draw.rect(maze_surface, WHITE, (x, y, TILE_SZ, TILE_SZ))
                elif cell == 'G':
                    pygame.draw.rect(maze_surface, BLUE, (x, y, TILE_SZ, TILE_SZ))
                elif cell == 'P':
                    pygame.draw.rect(maze_surface, BLACK, (x, y, TILE_SZ, TILE_SZ))

        running = True
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

    # def game_over_text(self):
    #     over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    #     screen.blit(over_text, (200, 250))


