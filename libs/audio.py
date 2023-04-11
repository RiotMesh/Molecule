import pygame as pg

from libs import console
from libs.language import lang


class MoleculeAudio:

    def __init__(self, sound_path):
        self.sound_path = sound_path
        try:
            self.sound = pg.mixer.Sound(self.sound_path)
        except Exception as ex:
            if lang() == "en":
                console.error(
                    f"Error occurred when try to laod sound -> {self.sound_path}\nError info >> {ex.__str__()}")
            else:
                console.error(
                    f"Произошла ошибка при загрузке звукового файла -> {self.sound_path}\nОшибка >> {ex.__str__()}")

    @staticmethod
    def play_once(path, volume):
        pg.mixer.init()
        sound = pg.mixer.Sound(path)
        sound.set_volume(volume)
        sound.play()

    def play(self, volume=1.0, loop=False):
        self.sound.set_volume(volume)
        self.sound.play(loops=loop)

    def stop(self):
        self.sound.stop()

    def length(self):
        return self.sound.get_length()
