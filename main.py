# pygame disable console prompt
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


# imports
from libs import config
from libs import console
from libs.language import lang
import pygame as pg


# initialization
pg.mixer.pre_init()
pg.init()
pg.mixer.init()

if lang() == "en":
    input("Molecule was initialized! Press ENTER to continue...")
else:
    input("Molecule загружена! Нажмите ENTER для продолжения...")

# pre-methods
# TODO: PRE-METHODS LIKE FIRST TIME


# startup main program
console.success("Example message for testing print effect!")
