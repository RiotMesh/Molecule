from threading import Thread
import pygame as pg
from libs import config
from libs.audio import MoleculeAudio
from time import sleep


class PrintFX:

    def __init__(self, text_length):
        self.steps = round((text_length * config.mget("print_effect_delay")) / config.mget("print_effect_sound_delay"))
        self.steps = 2 if self.steps < 2 else self.steps

        # pg.mixer.init()

        self.sound = pg.mixer.Sound("system/sounds/print.wav")
        self.sound.set_volume(config.mget("print_effect_sound_volume"))
        self.sound_delay = config.mget("print_effect_sound_delay")

        self.__thread = Thread(target=self.__fx_thread())

    def __fx_thread(self):
        i = 1
        print("FX THREAD STARTED!")
        while i <= self.steps:
            self.sound.play()
            i += 1
            sleep(self.sound_delay)

    def play(self):
        self.__thread.start()
