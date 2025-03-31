from plugins.astar_ghost import astarGhost
from plugins.bfs_ghost import bfsGhost


class GhostAIManager:
    def __init__(self):
        self.ghost_strategies = {
            "BFS": bfsGhost(),
            "A*": astarGhost(),
        }

    def get_ai(self, level):
        return self.ghost_strategies[level]
