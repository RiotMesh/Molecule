from libs import config
from libs.console import MoleculeConsole
from libs.language import lang

# initialization
console = MoleculeConsole()

# main program
console.message("Molecule launched!")
console.warning(config.mget("shell.name"))
