import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)  # pg.mouse.set_cursor(*pg.cursors.broken_x)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)  # noqa
        self.player = Player(self)  # noqa
        self.object_renderer = ObjectRenderer(self)  # noqa
        self.raycasting = RayCasting(self)  # noqa
        self.object_handler = ObjectHandler(self)  # noqa
        self.weapon = Weapon(self) # noqa
        self.sound = Sound(self)  # noqa
        self.pathfinding = PathFinding(self)  # noqa

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'Running {self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')  # 2D
        self.object_renderer.draw()  # 3D
        self.weapon.draw()  # 3D
        # self.map.draw()  # 2D
        # self.player.draw()  # 2D

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()