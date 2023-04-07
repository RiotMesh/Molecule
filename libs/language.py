def lang(language=None):
    if language is None:
        with open("language.txt", 'r') as lang_file:
            value = lang_file.read()
            value = value.split("\n")
            return value[2]
    else:
        with open("language.txt", 'rw') as lang_file:
            value = lang_file.read()
            value = value.split("\n")
            value[2] = language
            lang_file.write(f"{value[0]}\n{value[1]}\n{value[2]}")