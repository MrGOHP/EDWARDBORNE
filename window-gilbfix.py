"""
EDWARDBORNE
"""
import arcade
from arcade.examples.sprite_bullets_aimed import SCREEN_HEIGHT, SCREEN_TITLE
from arcade.examples.sprite_move_animation import CHARACTER_SCALING
from arcade.examples.sprite_tiled_map import TILE_SCALING

SCREEN_WIDTH = 800  # RG - Added SCREEN_WIDTH constant for window width
SCREEN_HEIGHT = 600  # RG - Added SCREEN_HEIGHT constant for window height
SCREEN_TITLE = "EDWARDBORNE"  # RG - Added SCREEN_TITLE constant for window title
CHARACTER_SCALING = 1  # RG - Added CHARACTER_SCALING constant for scaling character sprites
TILE_SCALING = 0.5  # RG - Added TILE_SCALING constant for scaling tile sprites

class EDWARDBORNE(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.wall_list = None
        self.player_list = None
        self.player_sprite = None
        arcade.set_background_color(arcade.csscolor.DIM_GRAY)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        # RG - Removed unused variable 'image_source' as it is not needed
        # self.player_sprite = arcade.Sprite("/home/brody/PycharmProjects/vEdwardsBornev/images/player_stand.png", CHARACTER_SCALING)
        # RG - Changed the sprite path to use a relative path or built-in resource
        # RG - So, this isn't your sprite, if you relative yours after this it should work.
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", CHARACTER_SCALING)
        # RG - Using a built-in resource ensures the path works on any machine

        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        for x in range(0, 1250, 64):
            # ... rest of your code ...
            pass  # RG - Placeholder for the rest of your code

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.player_list.draw()

def main():
    window = EDWARDBORNE()
    window.setup()
    window.run()

if __name__ == "__main__":
    main()
