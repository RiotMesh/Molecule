import json
from libs.language import lang
from libs.console import MoleculeConsole

console = MoleculeConsole()


def mget(path):
    try:
        with open("config.json", 'r') as config_file:
            json_string = config_file.read()
        config = json.loads(json_string)
        return config["molecule"][path]
    except Exception as e:
        if lang() == "en":
            console.error(f"Error occurred while try to get config -> molecule.{path}\n"
                          f"Check the correctness of the passed parameter and the presence of the config.json file\n"
                          f"Error info >> {e.__str__()}")
        else:
            console.error(f"Произошла ошибка во время чтения настройки -> molecule.{path}\n"
                          f"Проверьте корректность переданного параметра и наличие файла config.json\n"
                          f"Ошибка >> {e.__str__()}")


def mset(path):
    pass