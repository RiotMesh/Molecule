from colorama import Fore, Back, Style, init as initColorama
from libs.language import lang
from libs import config
from time import sleep

class MoleculeConsole:

    def __init__(self):
        self.shell_name = "Molecule"
        self.shell_info = "MESSAGE" if lang() == "en" else "ВЫВОД"
        self.shell_warning = "WARNING" if lang() == "en" else "ВНИМАНИЕ"
        self.shell_error = "ERROR" if lang() == "en" else "ОШИБКА"
        self.shell_success = "SUCCESS" if lang() == "en" else "УСПЕШНО"

        self.color_default = Style.RESET_ALL
        self.color_molecule = Fore.LIGHTBLUE_EX
        self.color_warning = Fore.LIGHTYELLOW_EX
        self.color_error = Fore.LIGHTRED_EX
        self.color_success = Fore.LIGHTGREEN_EX

    def message(self, text):
        if config.mget("shell.print_effect"):
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.shell_info} ]\n"
            print(outline, end="")

            print_effect_delay = config.mget("shell.print_effect.delay")
            for symbol in text:
                print(symbol, end="", flush=True)
                sleep(print_effect_delay)
            print("", end="\n\n" if config.mget("shell.separate_output") else "\n")
        else:
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.shell_info} ]\n{text}"
            print(outline, end="\n\n" if config.mget("shell.separate_output") else "\n")

    def warning(self, text):
        if config.mget("shell.print_effect"):
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_warning}{self.shell_warning}{self.color_default} ]\n"
            print(outline + self.color_warning, end="")

            print_effect_delay = config.mget("shell.print_effect.delay")
            for symbol in text:
                print(symbol, end="", flush=True)
                sleep(print_effect_delay)
            print(self.color_default, end="\n\n" if config.mget("shell.separate_output") else "\n")
        else:
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_warning}{self.shell_warning}{self.color_default} ]\n" \
                      f"{self.color_warning}{text}{self.color_default}"
            print(outline, end="\n\n" if config.mget("shell.separate_output") else "\n")

    def error(self, text):
        if config.mget("shell.print_effect"):
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_error}{self.shell_error}{self.color_default} ]\n"
            print(outline + self.color_error, end="")

            print_effect_delay = config.mget("shell.print_effect.delay")
            for symbol in text:
                print(symbol, end="", flush=True)
                sleep(print_effect_delay)
            print(self.color_default, end="\n\n" if config.mget("shell.separate_output") else "\n")
        else:
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_error}{self.shell_error}{self.color_error} ]\n" \
                      f"{self.color_error}{text}{self.color_default}"
            print(outline, end="\n\n" if config.mget("shell.separate_output") else "\n")

    def success(self, text):
        if config.mget("shell.print_effect"):
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_success}{self.shell_success}{self.color_default} ]\n"
            print(outline + self.color_success, end="")

            print_effect_delay = config.mget("shell.print_effect.delay")
            for symbol in text:
                print(symbol, end="", flush=True)
                sleep(print_effect_delay)
            print(self.color_default, end="\n\n" if config.mget("shell.separate_output") else "\n")
        else:
            outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_success}{self.shell_success}{self.color_success} ]\n" \
                      f"{self.color_success}{text}{self.color_default}"
            print(outline, end="\n\n" if config.mget("shell.separate_output") else "\n")
