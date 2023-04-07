from colorama import Fore, Back, Style, init as initColorama
from libs.language import lang


class MoleculeConsole:

    def __init__(self):
        self.shell_name = "Molecule"
        self.shell_info = "MESSAGE" if lang() == "en" else "ВЫВОД"
        self.shell_warning = "WARNING" if lang() == "en" else "ВНИМАНИЕ"
        self.shell_error = "ERROR" if lang() == "en" else "ОШИБКА"

        self.color_default = Style.RESET_ALL
        self.color_molecule = Fore.LIGHTBLUE_EX
        self.color_warning = Fore.LIGHTYELLOW_EX
        self.color_error = Fore.LIGHTRED_EX

    def message(self, text, endline=True):
        outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.shell_info} ]\n{text}"
        print(outline, end="\n" if endline else "")

    def warning(self, text, endline=True):
        outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_warning}{self.shell_warning}{self.color_default} ]\n" \
                  f"{self.color_warning}{text}{self.color_default}"
        print(outline, end="\n" if endline else "")

    def error(self, text, endline=True):
        outline = f"[ {self.color_molecule}{self.shell_name}{self.color_default} >> {self.color_error}{self.shell_error}{self.color_default} ]\n" \
                  f"{self.color_error}{text}{self.color_default}"
        print(outline, end="\n" if endline else "")
