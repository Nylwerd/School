# Requirement 3d
class GameStats:
    """Statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initiate stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion when active is True
        self.game_active = False

        # High score should never be reset
        # Noah said his score beat the game so now it's forever the high score
        self.high_score = 89900

    def reset_stats(self):
        """Initiate Stats that change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1