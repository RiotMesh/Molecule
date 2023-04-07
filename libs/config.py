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
    except Exception as ex:
        if lang() == "en":
            console.error(f"Error occurred while try to get config -> molecule.{path}\n"
                          f"Check the correctness of the passed parameter and the presence of the config.json file\n"
                          f"Error info >> {ex.__str__()}")
        else:
            console.error(f"Произошла ошибка во время чтения настройки -> molecule.{path}\n"
                          f"Проверьте корректность переданного параметра и наличие файла config.json\n"
                          f"Ошибка >> {ex.__str__()}")


def mset(path, value):
    try:
        with open("config.json", 'r+') as config_file:
            json_string = config_file.read()

        config = json.loads(json_string)
        config["molecule"][path] = value

        with open("config.json", 'w') as config_file:
            config_file.write(json.dumps(config, indent=2))

        return True
    except Exception as ex:
        if lang() == "en":
            console.error(f"Error occurred while try to set config -> molecule.{path} = {value}\n"
                          f"Check the correctness of the passed parameters and the presence of the config.json file\n"
                          f"Error info >> {ex.__str__()}")
        else:
            console.error(f"Произошла ошибка во время записи настройки -> molecule.{path}\n"
                          f"Проверьте корректность переданных параметров и наличие файла config.json\n"
                          f"Ошибка >> {ex.__str__()}")


def uget(path):
    try:
        with open("config.json", 'r') as config_file:
            json_string = config_file.read()
        config = json.loads(json_string)
        return config["user"][path]
    except Exception as ex:
        if lang() == "en":
            console.error(f"Error occurred while try to get config -> user.{path}\n"
                          f"Check the correctness of the passed parameter and the presence of the config.json file\n"
                          f"Error info >> {ex.__str__()}")
        else:
            console.error(f"Произошла ошибка во время чтения настройки -> user.{path}\n"
                          f"Проверьте корректность переданного параметра и наличие файла config.json\n"
                          f"Ошибка >> {ex.__str__()}")


def uset(path, value):
    try:
        with open("config.json", 'r+') as config_file:
            json_string = config_file.read()

        config = json.loads(json_string)
        config["user"][path] = value

        with open("config.json", 'w') as config_file:
            config_file.write(json.dumps(config, indent=2))

        return True
    except Exception as ex:
        if lang() == "en":
            console.error(f"Error occurred while try to set config -> user.{path} = {value}\n"
                          f"Check the correctness of the passed parameters and the presence of the config.json file\n"
                          f"Error info >> {ex.__str__()}")
        else:
            console.error(f"Произошла ошибка во время записи настройки -> user.{path}\n"
                          f"Проверьте корректность переданных параметров и наличие файла config.json\n"
                          f"Ошибка >> {ex.__str__()}")