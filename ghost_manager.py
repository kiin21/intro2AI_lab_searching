import importlib


def load_plugin(ai_name):
    """Dynamically load a ghost AI plugin"""
    try:
        module = importlib.import_module(f"plugins.{ai_name}")
        algorithm = ai_name.split("_")[0]
        return getattr(module, algorithm + "Ghost")()

    except (ModuleNotFoundError, AttributeError):
        print(f"Error: Plugin '{ai_name}' not found.")
        return None


class GhostManager:
    def __init__(self, ai_name):
        self.ai_name = ai_name
        self.ghost_ai = load_plugin(ai_name)

    def move_ghost(self, game_state):
        if self.ghost_ai:
            return self.ghost_ai.move(game_state)
