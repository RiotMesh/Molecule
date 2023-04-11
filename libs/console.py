from colorama import Fore, Back, Style, init as initColorama

from libs.audiofx import PrintFX
from libs.language import lang
from libs import config
from time import sleep

shell_name = "Molecule"
shell_info = "MESSAGE" if lang() == "en" else "ВЫВОД"
shell_warning = "WARNING" if lang() == "en" else "ВНИМАНИЕ"
shell_error = "ERROR" if lang() == "en" else "ОШИБКА"
shell_success = "SUCCESS" if lang() == "en" else "УСПЕШНО"

color_default = Style.RESET_ALL
color_molecule = Fore.LIGHTBLUE_EX
color_warning = Fore.LIGHTYELLOW_EX
color_error = Fore.LIGHTRED_EX
color_success = Fore.LIGHTGREEN_EX


def message(text):
    if config.mget("print_effect"):
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {shell_info} ]\n"
        print(outline, end="")

        print_effect_delay = config.mget("print_effect_delay")
        for symbol in text:
            print(symbol, end="", flush=True)
            sleep(print_effect_delay)
        print("", end="\n\n" if config.mget("separate_output") else "\n")
    else:
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {shell_info} ]\n{text}"
        print(outline, end="\n\n" if config.mget("separate_output") else "\n")


def warning(text):
    if config.mget("print_effect"):
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {color_warning}{shell_warning}{color_default} ]\n"
        print(outline + color_warning, end="")

        print_effect_delay = config.mget("print_effect_delay")
        for symbol in text:
            print(symbol, end="", flush=True)
            sleep(print_effect_delay)
        print(color_default, end="\n\n" if config.mget("separate_output") else "\n")
    else:
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {color_warning}{shell_warning}{color_default} ]\n" \
                  f"{color_warning}{text}{color_default}"
        print(outline, end="\n\n" if config.mget("separate_output") else "\n")


def error(text):
    if config.mget("print_effect"):
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {color_error}{shell_error}{color_default} ]\n"
        print(outline + color_error, end="")

        print_effect_delay = config.mget("print_effect_delay")
        for symbol in text:
            print(symbol, end="", flush=True)
            sleep(print_effect_delay)
        print(color_default, end="\n\n" if config.mget("separate_output") else "\n")
    else:
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {color_error}{shell_error}{color_error} ]\n" \
                  f"{color_error}{text}{color_default}"
        print(outline, end="\n\n" if config.mget("separate_output") else "\n")


def success(text, need_input = False):
    if config.mget("print_effect"):
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {color_success}{shell_success}{color_default} ]\n"
        print(outline + color_success, end="")

        if config.mget("print_effect_sound"):
            PrintFX(len(text)).play()

        print_effect_delay = config.mget("print_effect_delay")
        for symbol in text:
            print(symbol, end="", flush=True)
            sleep(print_effect_delay)

        print(color_default, end="\n\n" if config.mget("separate_output") else "\n")
    else:
        outline = f"[ {color_molecule}{shell_name}{color_default} >> {color_success}{shell_success}{color_success} ]\n" \
                  f"{color_success}{text}{color_default}"
        print(outline, end="\n\n" if config.mget("separate_output") else "\n")

    if need_input:
        return input(" >>>> ")