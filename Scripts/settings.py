class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1350
        self.screen_height = 800
        self.bg_color =(230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10 # vertical speed

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 0.6
        self.bullet_speed = 1.5

        self.alien_speed = 0.3
        self.alien_points = 50

        self.fleet_direction = 1  # 1 is right, -1 is left

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)