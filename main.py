import sys

from cli import run_cli
from gui import run_gui

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli()
    else:
        run_gui()

# https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/