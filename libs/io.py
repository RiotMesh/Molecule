from colorama import Fore, Back, Style, init as initColorama

class MoleculaIO():

    def __init__(self, username):
        self.username = username
        self.shell_name = "Molecula"
        self.shell_info = "MESSAGE"
        self.shell_warning = "WARNING"
        self.shell_error = "ERROR"

        self.color_default = Style.RESET_ALL
        self.color_molecula = Fore.LIGHTBLUE_EX
        self.color_warning = Fore.LIGHTYELLOW_EX
        self.color_error = Fore.LIGHTRED_EX

    def message(self, text, endline = True):
        outline = f"[ {self.color_molecula}{self.shell_name}{self.color_default} >> {self.shell_info} ]\n{text}"
        print(outline, end="\n" if endline else "")

    def warning(self, text, endline = True):
        outline = f"[ {self.color_molecula}{self.shell_name}{self.color_default} >> {self.color_warning}{self.shell_warning}{self.color_default} ]\n{text}"
        print(outline, end="\n" if endline else "")

    def error(self, text, endline = True):
        outline = f"[ {self.color_molecula}{self.shell_name}{self.color_default} >> {self.color_error}{self.shell_error}{self.color_default} ]\n{text}"
        print(outline, end="\n" if endline else "")

    def TODO():
        pass # MAYBE NEED TO MAKE MORE METHODS FOR THIS CLASS, IDK...