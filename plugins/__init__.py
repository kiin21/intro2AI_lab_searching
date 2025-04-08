from plugins.astar_ghost import astarGhost
from plugins.bfs_ghost import bfsGhost
from plugins.dfs_ghost import dfsGhost

class GhostAIManager:
    def __init__(self):
        self.ghost_strategies = {
            "BFS": bfsGhost(),
            "A*": astarGhost(),
            "DFS": dfsGhost(),
            "UCS": ucsGhost(),
        }

    def get_ai(self, level):
        return self.ghost_strategies[level]
